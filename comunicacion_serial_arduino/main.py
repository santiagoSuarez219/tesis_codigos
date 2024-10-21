import serial
import time

# Configura el puerto serial (reemplaza '/dev/ttyACM0' con el puerto correcto)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Espera a que la conexión serial se inicie

try:
    # Enviar mensaje al Arduino
    while True:
        value_heater = input("Ingrese el valor del calentador (0 o 255): ")
        message = f"{value_heater}\n"
        ser.write(message.encode('utf-8'))
        
        # Esperar la respuesta del Arduino
        while True:
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Respuesta recibida del Arduino: {response}")
                break

except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()
