from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PySide6.QtCore import QThread, Signal
from matplotlib.figure import Figure
import numpy as np
import time

class ContenedorGrafica(QThread):
    def __init__(self, grafica):
        super(ContenedorGrafica, self).__init__() 
        self.grafica = grafica
        self.data_maxima_temperatura = []
    
    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(.050)

    def actualizar_datos(self):
        if len(self.data_maxima_temperatura) == 100:
            self.data_maxima_temperatura.pop(0)
        self.grafica.actualizar_graficas(self.data_maxima_temperatura)


class GraficaTemperaturaMaxima(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure(layout='tight')  
        super(GraficaTemperaturaMaxima, self).__init__(figura)
        self.g = figura.add_subplot(111)  
        
        
        
    def actualizar_graficas(self, data):
        self.g.clear()
        self.g.plot(data, '-o')
        self.g.set_ylim(25, 50)
        self.g.set_xlim(0, 100)
        self.g.grid()
        self.g.set_title("Temperatura Maxima (°C)", fontsize=10)
        self.g.tick_params(axis='both', which='major', labelsize=8)
        self.g.get_xaxis().set_visible(False)
        self.g.set_facecolor('#EFEFEF')  # Fondo de la zona de los ejes
        self.figure.set_facecolor('#EFEFEF')  
        self.draw()
