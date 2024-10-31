from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from picamera2 import Picamera2
import time 
import cv2

class ImagenRGB(QThread):
    Imageupd = Signal(QImage)
    def __init__(self):
        super(ImagenRGB, self).__init__()
        self.hilo_corriendo = True
        self.piCam = Picamera2()
        self.piCam.preview_configuration.main.size = (1280, 720)
        self.piCam.preview_configuration.main.format = "RGB888"
        self.piCam.preview_configuration.align()
        self.piCam.configure("preview")
        self.piCam.start()


    def run(self):
        while self.hilo_corriendo:
            frame = self.piCam.capture_array()
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.Imageupd.emit(q_image)

    def stop(self):
        self.hilo_corriendo = False
        self.piCam.stop()
        self.quit()
        self.wait()