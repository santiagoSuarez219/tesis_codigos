# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowgcdRlM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.frame_visual = QFrame(self.main_frame)
        self.frame_visual.setObjectName(u"frame_visual")
        self.frame_visual.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_visual.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_visual)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_cameras = QFrame(self.frame_visual)
        self.frame_cameras.setObjectName(u"frame_cameras")
        self.frame_cameras.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cameras.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_cameras)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)


        self.tab_cameras = QTabWidget(self.frame_cameras)
        self.tab_cameras.setObjectName(u"tab_cameras")
        self.tab_thermal_image = QWidget()
        self.tab_thermal_image.setObjectName(u"tab_thermal_image")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_thermal_image)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.thermal_image = QFrame(self.tab_thermal_image)
        self.thermal_image.setObjectName(u"thermal_image")
        self.thermal_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.thermal_image.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.thermal_image)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.layout_thermal_image = QVBoxLayout()
        self.layout_thermal_image.setObjectName(u"layout_thermal_image")

        self.verticalLayout_7.addLayout(self.layout_thermal_image)


        self.horizontalLayout_16.addWidget(self.thermal_image)

        self.horizontalLayout_16.setStretch(0, 10)
        self.tab_cameras.addTab(self.tab_thermal_image, "")
        self.tab_RGB_image = QWidget()
        self.tab_RGB_image.setObjectName(u"tab_RGB_image")
        self.verticalLayoutWidget = QWidget(self.tab_RGB_image)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 600, 600))
        self.layout_RGB_image = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_RGB_image.setObjectName(u"layout_RGB_image")
        self.layout_RGB_image.setContentsMargins(0, 0, 0, 0)
        self.layout_RGB_image.setSpacing(0)
        self.layout_RGB_image.setStretch(0, 1)
        
        self.tab_cameras.addTab(self.tab_RGB_image, "")
        self.verticalLayout_2.addWidget(self.tab_cameras)

        self.label_rgb_image = QLabel(self.tab_RGB_image)
        self.label_rgb_image.setObjectName("label_rgb_image")
        self.label_rgb_image.setAlignment(Qt.AlignCenter)
        self.layout_RGB_image.addWidget(self.label_rgb_image)

        self.horizontalLayout_2.addWidget(self.frame_cameras)
        self.frame_temperature_graphics = QFrame(self.frame_visual)
        self.frame_temperature_graphics.setObjectName(u"frame_temperature_graphics")
        self.frame_temperature_graphics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_temperature_graphics.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_temperature_graphics)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.frame_max_temperature = QFrame(self.frame_temperature_graphics)
        self.frame_max_temperature.setObjectName(u"frame_max_temperature")
        self.frame_max_temperature.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_max_temperature.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_max_temperature)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.max_temperature_container = QWidget(self.frame_max_temperature)
        self.max_temperature_container.setObjectName(u"max_temperature_container")
        self.verticalLayout_8 = QVBoxLayout(self.max_temperature_container)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_max_temperature = QVBoxLayout()
        self.vertical_layout_max_temperature.setObjectName(u"vertical_layout_max_temperature")
        self.verticalLayout_8.addLayout(self.vertical_layout_max_temperature)
        self.horizontalLayout_7.addWidget(self.max_temperature_container)
        self.verticalLayout_5.addWidget(self.frame_max_temperature)

        self.frame_mean_temperature = QFrame(self.frame_temperature_graphics)
        self.frame_mean_temperature.setObjectName(u"frame_mean_temperature")
        self.frame_mean_temperature.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_mean_temperature.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_mean_temperature)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mean_temperature_container = QWidget(self.frame_mean_temperature)
        self.mean_temperature_container.setObjectName(u"mean_temperature_container")
        self.verticalLayout_9 = QVBoxLayout(self.mean_temperature_container)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_mean_temperature = QVBoxLayout()
        self.vertical_layout_mean_temperature.setObjectName(u"vertical_layout_mean_temperature")
        self.verticalLayout_9.addLayout(self.vertical_layout_mean_temperature)
        self.horizontalLayout_8.addWidget(self.mean_temperature_container)
        self.verticalLayout_5.addWidget(self.frame_mean_temperature)


        self.horizontalLayout_2.addWidget(self.frame_temperature_graphics)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 2)

        self.horizontalLayout.addWidget(self.frame_visual)

        self.frame_user = QFrame(self.main_frame)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_user.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_user)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_thermal_params = QFrame(self.frame_user)
        self.frame_thermal_params.setObjectName(u"frame_thermal_params")
        self.frame_thermal_params.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_thermal_params.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_thermal_params)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.parametros_termicos_label = QLabel(self.frame_thermal_params)
        self.parametros_termicos_label.setObjectName(u"parametros_termicos_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.parametros_termicos_label.setFont(font)

        self.verticalLayout_4.addWidget(self.parametros_termicos_label)

        self.frame = QFrame(self.frame_thermal_params)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.temperatura_maxima = QLabel(self.frame)
        self.temperatura_maxima.setObjectName(u"temperatura_maxima")
        font1 = QFont()
        font1.setPointSize(10)
        self.temperatura_maxima.setFont(font1)

        self.horizontalLayout_9.addWidget(self.temperatura_maxima)

        self.temperatura_maxima_value = QLabel(self.frame)
        self.temperatura_maxima_value.setObjectName(u"temperatura_maxima_value")
        self.temperatura_maxima_value.setFont(font1)
        self.temperatura_maxima_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.temperatura_maxima_value)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_thermal_params)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.temperatura_minima = QLabel(self.frame_2)
        self.temperatura_minima.setObjectName(u"temperatura_minima")
        self.temperatura_minima.setFont(font1)

        self.horizontalLayout_10.addWidget(self.temperatura_minima)

        self.temperatura_minima_value = QLabel(self.frame_2)
        self.temperatura_minima_value.setObjectName(u"temperatura_minima_value")
        self.temperatura_minima_value.setFont(font1)
        self.temperatura_minima_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.temperatura_minima_value)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_thermal_params)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.temperatura_promedio = QLabel(self.frame_3)
        self.temperatura_promedio.setObjectName(u"temperatura_promedio")
        self.temperatura_promedio.setFont(font1)

        self.horizontalLayout_11.addWidget(self.temperatura_promedio)

        self.temperatura_promedio_value = QLabel(self.frame_3)
        self.temperatura_promedio_value.setObjectName(u"temperatura_promedio_value")
        self.temperatura_promedio_value.setFont(font1)
        self.temperatura_promedio_value.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.temperatura_promedio_value)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_thermal_params)

        self.frame_4 = QFrame(self.frame_user)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_12.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_sensibility_range = QFrame(self.frame_user)
        self.frame_sensibility_range.setObjectName(u"frame_sensibility_range")
        self.frame_sensibility_range.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sensibility_range.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_sensibility_range)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_sensibility_range = QLabel(self.frame_sensibility_range)
        self.label_sensibility_range.setObjectName(u"label_sensibility_range")

        self.horizontalLayout_13.addWidget(self.label_sensibility_range)

        self.sensibility_inferior_range_value = QDoubleSpinBox(self.frame_sensibility_range)
        self.sensibility_inferior_range_value.setObjectName(u"sensibility_inferior_range_value")

        self.horizontalLayout_13.addWidget(self.sensibility_inferior_range_value)


        self.verticalLayout_3.addWidget(self.frame_sensibility_range)

        self.frame_5 = QFrame(self.frame_user)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_sensibility_range_superior = QLabel(self.frame_5)
        self.label_sensibility_range_superior.setObjectName(u"label_sensibility_range_superior")

        self.horizontalLayout_14.addWidget(self.label_sensibility_range_superior)

        self.sensibility_range_superior_value = QDoubleSpinBox(self.frame_5)
        self.sensibility_range_superior_value.setObjectName(u"sensibility_range_superior_value")

        self.horizontalLayout_14.addWidget(self.sensibility_range_superior_value)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_control_params = QFrame(self.frame_user)
        self.frame_control_params.setObjectName(u"frame_control_params")
        self.frame_control_params.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_control_params.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_control_params)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.control_temperatura_label = QLabel(self.frame_control_params)
        self.control_temperatura_label.setObjectName(u"control_temperatura_label")
        self.control_temperatura_label.setFont(font)

        self.verticalLayout_6.addWidget(self.control_temperatura_label)

        self.setpoint_label = QLabel(self.frame_control_params)
        self.setpoint_label.setObjectName(u"setpoint_label")

        self.verticalLayout_6.addWidget(self.setpoint_label)

        self.setpoint_value = QSpinBox(self.frame_control_params)
        self.setpoint_value.setObjectName(u"setpoint_value")

        self.verticalLayout_6.addWidget(self.setpoint_value)

        self.frame_P_control = QFrame(self.frame_control_params)
        self.frame_P_control.setObjectName(u"frame_P_control")
        self.frame_P_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_P_control.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_P_control)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.control_P_label = QLabel(self.frame_P_control)
        self.control_P_label.setObjectName(u"control_P_label")

        self.horizontalLayout_3.addWidget(self.control_P_label)

        self.control_P_value = QDoubleSpinBox(self.frame_P_control)
        self.control_P_value.setObjectName(u"control_P_value")

        self.horizontalLayout_3.addWidget(self.control_P_value)


        self.verticalLayout_6.addWidget(self.frame_P_control)

        self.frame_I_control = QFrame(self.frame_control_params)
        self.frame_I_control.setObjectName(u"frame_I_control")
        self.frame_I_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_I_control.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_I_control)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.control_I_label = QLabel(self.frame_I_control)
        self.control_I_label.setObjectName(u"control_I_label")

        self.horizontalLayout_4.addWidget(self.control_I_label)

        self.control_I_value = QDoubleSpinBox(self.frame_I_control)
        self.control_I_value.setObjectName(u"control_I_value")

        self.horizontalLayout_4.addWidget(self.control_I_value)


        self.verticalLayout_6.addWidget(self.frame_I_control)

        self.frame_D_control = QFrame(self.frame_control_params)
        self.frame_D_control.setObjectName(u"frame_D_control")
        self.frame_D_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_D_control.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_D_control)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.control_D_label = QLabel(self.frame_D_control)
        self.control_D_label.setObjectName(u"control_D_label")

        self.horizontalLayout_5.addWidget(self.control_D_label)

        self.control_D_value = QDoubleSpinBox(self.frame_D_control)
        self.control_D_value.setObjectName(u"control_D_value")

        self.horizontalLayout_5.addWidget(self.control_D_value)


        self.verticalLayout_6.addWidget(self.frame_D_control)

        self.pushButton = QPushButton(self.frame_control_params)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.frame_control_params)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_control_params)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.frame_time = QFrame(self.frame_control_params)
        self.frame_time.setObjectName(u"frame_time")
        self.frame_time.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_time.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_time)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.time_label = QLabel(self.frame_time)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout_6.addWidget(self.time_label)

        self.time_value = QLabel(self.frame_time)
        self.time_value.setObjectName(u"time_value")
        self.time_value.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_6.addWidget(self.time_value)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_6.addWidget(self.frame_time)


        self.verticalLayout_3.addWidget(self.frame_control_params)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(4, 2)

        self.horizontalLayout.addWidget(self.frame_user)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1130, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_cameras.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Terapia Hipertermia", None))
        self.tab_cameras.setTabText(self.tab_cameras.indexOf(self.tab_thermal_image), QCoreApplication.translate("MainWindow", u"IR", None))
        self.tab_cameras.setTabText(self.tab_cameras.indexOf(self.tab_RGB_image), QCoreApplication.translate("MainWindow", u"RGB", None))
        self.parametros_termicos_label.setText(QCoreApplication.translate("MainWindow", u"Parametros termicos", None))
        self.temperatura_maxima.setText(QCoreApplication.translate("MainWindow", u"Temperatura maxima:", None))
        self.temperatura_maxima_value.setText(QCoreApplication.translate("MainWindow", u"43 \u00b0C", None))
        self.temperatura_minima.setText(QCoreApplication.translate("MainWindow", u"Temperatura minima:", None))
        self.temperatura_minima_value.setText(QCoreApplication.translate("MainWindow", u"36 \u00b0C", None))
        self.temperatura_promedio.setText(QCoreApplication.translate("MainWindow", u"Temperatura promedio", None))
        self.temperatura_promedio_value.setText(QCoreApplication.translate("MainWindow", u"35 \u00b0C", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rango de sensibilidad", None))
        self.label_sensibility_range.setText(QCoreApplication.translate("MainWindow", u"Limite inferior", None))
        self.label_sensibility_range_superior.setText(QCoreApplication.translate("MainWindow", u"Limite superior", None))
        self.control_temperatura_label.setText(QCoreApplication.translate("MainWindow", u"Control de temperatura", None))
        self.setpoint_label.setText(QCoreApplication.translate("MainWindow", u"Temperatura deseada", None))
        self.control_P_label.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.control_I_label.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.control_D_label.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"INICIAR TERAPIA", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"DETENER TERAPIA", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido", None))
        self.time_value.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
    # retranslateUi

