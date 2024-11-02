from PySide6.QtCore import QThread
import pandas as pd
import numpy as np
import serial
import time

class ControlTemperatura(QThread):
    def __init__(self):
        super(ControlTemperatura, self).__init__()
        self.temperatura_camara = 0.0
        self.setpoint_value = 0.0
        self.running = False

    
    def run(self):
        self.start_control()
        ITAE = 0.0
        start_time = time.time()
        prev_time = start_time
        dt_error = 0.0
        ierr = 0.0
        try:
            i = 0
            while self.running:
                t = time.time()
                dt = t - prev_time 
                prev_time = t
                self.tm[i] = t - start_time
                self.T1[i] = self.temperatura_camara
                [self.Q1[i],P,ierr,D] = self.pid(self.setpoint[i],self.T1[i],self.T1[i-1],ierr,dt)
                print(f"Q1: {self.Q1[i]}")
                ITAE = ITAE + (abs(self.setpoint-self.T1[i]))*(i+1)
                self.data_csv['tm'].append(self.tm[i]) # Guardar datos en un diccionario para exportar a CSV cada segundo
                if self.temperatura_camara is not None:
                    self.data_csv['temperatura camara'].append(self.temperatura_camara)
                else:
                    self.data_csv['temperatura camara'].append(0.0)
                self.data_csv['setpoint'].append(self.setpoint[i])
                self.enviar_actuador(str(int(self.Q1[i]*255/100)))
                time.sleep(1)
                i += 1
        except Exception as e: 
            print(f'Error: {e}')     
            self.puerto_serie.write(str(0).encode())
            self.puerto_serie.close()

        return ITAE
    
    def connectToArduino(self):
        try:
            self.puerto_serie = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            time.sleep(2)
            print('Conectado al puerto serie')
        except:
            print('No se pudo conectar con el puerto serie')
    
    def start_control(self):
        self.connectToArduino()
        self.loops = int(60.0*30.0)
        self.setpoint = np.ones(self.loops) * self.setpoint_value
        self.tm = np.zeros(self.loops)
        self.T1 = np.ones(self.loops) * temperatura_camara
        self.error_sp = np.zeros(self.loops)
        self.Q1 = np.ones(self.loops) * 0.0
        self.running = True
        self.data_csv = {
            'tm':[],
            'setpoint': [],
            'temperatura camara': [],
        }
        self.prev_error = 0.0
        self.prev_prev_error = 0.0
        self.prev_output = 0.0

    
    def modificar_setpoint(self, setpoint):
        print(f"Setpoint modificado a {setpoint}")
        self.setpoint = np.ones(self.loops) * setpoint

    def pid(self,sp,pv,pv_last,ierr,dt):
        Kp = 0.5 
        Kc   = 10.0 
        tauI = 50.0 
        tauD = 1.0  
        KP = 16.0295
        KI = 0.021356
        KD = 0.009639
        op0 = 0 
        ophi = 100
        oplo = 0

        error = sp-pv
        ierr = ierr + KI * error * dt
        dpv = (pv - pv_last) / dt
        P = KP * error
        I = ierr
        D = -KD * dpv
        op = op0 + P + I + D

    
        if op < oplo or op > ophi:
            I = I - KI * error * dt
            op = max(oplo,min(ophi,op))
        return [op,P,I,D]
    
    def enviar_actuador(self, value):
        print(value)
        message = f"{value}\n"
        self.puerto_serie.write(message.encode('utf-8'))
    
    def stop_control(self):
        if self.running:
            self.running = False
            df = pd.DataFrame(self.data_csv)
            df.to_csv('data_control.csv')
            self.enviar_actuador(str(int(0*255/100)))
            time.sleep(2)
            self.puerto_serie.close()