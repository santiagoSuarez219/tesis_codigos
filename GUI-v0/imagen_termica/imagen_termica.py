import cv2
import numpy as np
from scipy.ndimage import zoom
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap, QMouseEvent, QPainter, QPen
from PySide6.QtCore import Qt, QRect, QThread, Signal
import sys


import board
import busio
import adafruit_mlx90640
import time

# Clase Grafica, la cual es un QLabel que muestra la imagen térmica y permite seleccionar un ROI
class Grafica(QLabel):
    def __init__(self):
        super(Grafica, self).__init__()
        self.data_imagen_termica = np.zeros((24, 32), dtype=np.float32)
        self.setScaledContents(True)         

    def actualizar_imagen(self, data_imagen_termica_interpolada):
        # Aplica el colormap tipo 'jet' para simular la visualización térmica
        imagen_coloreada = cv2.applyColorMap(np.uint8(data_imagen_termica_interpolada), cv2.COLORMAP_JET)
        
        # Convierte la imagen de BGR (por defecto en OpenCV) a RGB
        imagen_rgb = cv2.cvtColor(imagen_coloreada, cv2.COLOR_BGR2RGB)
        
        # Convierte la imagen a formato que PySide6 pueda usar
        h, w, ch = imagen_rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(imagen_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # Muestra la imagen en el QLabel
        self.setPixmap(QPixmap.fromImage(qimg))


class ImagenTermica(QThread):
    actualizar_labels_signal = Signal(float, float, float)

    def __init__(self, grafica):
        super(ImagenTermica, self).__init__()
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
        self.mlx = adafruit_mlx90640.MLX90640(self.i2c)
        print("MLX addr detected on I2C", [hex(i) for i in self.mlx.serial_number])
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
        self.frame = [0] * 768  # 32 * 24
        self.grafica = grafica
        self.mlx.getFrame(self.frame)
        self.data_imagen_termica = np.array(self.frame).reshape((24, 32))

    def run(self):
        while True:
            self.actualizar_datos()
            time.sleep(0.050)

    def actualizar_datos(self):
        self.mlx.getFrame(self.frame)
        self.data_imagen_termica = np.array(self.frame).reshape((24, 32))

        # Interpolación de la imagen para mejorar la resolución
        factor_zoom = 4  # Aumenta este valor para una mayor resolución
        data_interpolada = zoom(self.data_imagen_termica, factor_zoom)
        
        # Normaliza la imagen a un rango de 0 a 255 para aplicar el colormap
        data_interpolada_normalizada = cv2.normalize(data_interpolada, None, 0, 255, cv2.NORM_MINMAX)

        # Actualiza la imagen en la GUI usando OpenCV
        self.grafica.actualizar_imagen(data_interpolada_normalizada)
        
        # Calcula las temperaturas de la imagen
        maxima = np.max(self.data_imagen_termica)
        minima = np.min(self.data_imagen_termica)
        promedio = np.mean(self.data_imagen_termica)
        self.actualizar_labels_signal.emit(maxima, minima, promedio)