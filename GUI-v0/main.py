from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, Qt
import sys

from grafica_temperatura_promedio.grafica_temperatura_promedio import ContenedorGraficaPromedio, GraficaTemperaturaPromedio
from grafica_temperatura_maxima.grafica_temperatura_maxima import ContenedorGrafica, GraficaTemperaturaMaxima
from control_temperatura.control_temperatura import ControlTemperatura
from imagen_termica.imagen_termica import Grafica, ImagenTermica
from imagen_rgb.imagen_rgb import ImagenRGB

from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.control_temperatura = ControlTemperatura()

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

        # self.ImageRGB = ImagenRGB()
        # self.ImageRGB.start()
        # self.ImageRGB.Imageupd.connect(self.show_image)

        self.pushButton_2.clicked.connect(self.activar_control)
        self.pushButton_3.clicked.connect(self.desactivar_control)
        self.pushButton.clicked.connect(self.modificar_setpoint)

        
    def actualizar_labels_temperatura(self, maxima, minima, promedio):
        self.temperatura_maxima_value.setText(f"{maxima:.2f} °C")
        self.temperatura_minima_value.setText(f"{minima:.2f} °C")
        self.temperatura_promedio_value.setText(f"{promedio:.2f} °C")
        self.control_temperatura.temperatura_camara = maxima
        self.contenedor_grafica.data_maxima_temperatura.append(maxima)
        self.contenedor_grafica_promedio.data_promedio.append(promedio)

    def show_image(self, Image):
        scaled_image = Image.scaled(self.label_rgb_image.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label_rgb_image.setPixmap(QPixmap.fromImage(scaled_image))

    def activar_control(self):
        if self.verificar_setpoint(self.control_temperatura.setpoint_value):
            # TODO: Verificar rango de sensibilidad
            self.control_temperatura.start()
            

    def desactivar_control(self):
        self.control_temperatura.modificar_setpoint(0.0)
        self.control_temperatura.stop_control()
        self.control_temperatura.terminate()

    def modificar_setpoint(self):
        setpoint = float(self.setpoint_value.text())
        if verificar_setpoint(setpoint):
            self.control_temperatura.modificar_setpoint(setpoint)

    def verificar_setpoint(self, setpoint):
        if setpoint == 0.0:
            print("Setpoint no definido") # Cambiar por une ventana emergente
            return False
        if setpoint < 36.0 or setpoint > 46.0:
            print("Setpoint fuera de rango")
            return False
        return True

    def closeEvent(self, event):
        # TODO: Agregar un mensaje de confirmacion
        self.control_temperatura.stop_control()
        self.control_temperatura.terminate()
        self.control_temperatura.wait()
        # self.ImageRGB.terminate()
        # self.ImageRGB.wait()
        self.imagen_termica.terminate()
        self.imagen_termica.wait()
        self.contenedor_grafica.terminate()
        self.contenedor_grafica.wait()
        self.contenedor_grafica_promedio.terminate()
        self.contenedor_grafica_promedio.wait()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())