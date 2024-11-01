from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, Qt
import sys

from grafica_temperatura_promedio.grafica_temperatura_promedio import ContenedorGraficaPromedio, GraficaTemperaturaPromedio
from grafica_temperatura_maxima.grafica_temperatura_maxima import ContenedorGrafica, GraficaTemperaturaMaxima
from imagen_termica.imagen_termica import Grafica, ImagenTermica
from imagen_rgb.imagen_rgb import ImagenRGB

from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.grafica = Grafica()
        self.imagen_termica = ImagenTermica(self.grafica)
        self.imagen_termica.start()
        self.imagen_termica.actualizar_labels_signal.connect(self.actualizar_labels_temperatura)
        self.layout_thermal_image.addWidget(self.grafica)

        self.grafica_temperatura_maxima = GraficaTemperaturaMaxima()
        self.contenedor_grafica = ContenedorGrafica(self.grafica_temperatura_maxima)
        self.contenedor_grafica.start()
        self.verticalLayout_8.addWidget(self.grafica_temperatura_maxima)

        self.grafica_temperatura_promedio = GraficaTemperaturaPromedio()
        self.contenedor_grafica_promedio = ContenedorGraficaPromedio(self.grafica_temperatura_promedio)
        self.contenedor_grafica_promedio.start()
        self.verticalLayout_9.addWidget(self.grafica_temperatura_promedio)

        self.ImageRGB = ImagenRGB()
        self.ImageRGB.start()
        self.ImageRGB.Imageupd.connect(self.show_image)

        
    def actualizar_labels_temperatura(self, maxima, minima, promedio):
        self.temperatura_maxima_value.setText(f"{maxima:.2f} °C")
        self.temperatura_minima_value.setText(f"{minima:.2f} °C")
        self.temperatura_promedio_value.setText(f"{promedio:.2f} °C")
        self.contenedor_grafica.data_maxima_temperatura.append(maxima)
        self.contenedor_grafica_promedio.data_promedio.append(promedio)
        # if self.toggleControl.isChecked():
        #     self.control_temperatura.temperatura_camara = maxima

    def show_image(self, Image):
        scaled_image = Image.scaled(self.label_rgb_image.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_rgb_image.setPixmap(QPixmap.fromImage(scaled_image))


    # def closeEvent(self, event):
    #     self.imagen_termica.terminate()
    #     event.accept()




        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())