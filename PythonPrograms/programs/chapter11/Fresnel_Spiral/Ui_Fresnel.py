# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Fresnel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 648)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.SpinBox_a1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_a1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_a1.setDecimals(3)
        self.SpinBox_a1.setMinimum(1.0)
        self.SpinBox_a1.setMaximum(100.0)
        self.SpinBox_a1.setProperty("value", 10.0)
        self.SpinBox_a1.setObjectName("SpinBox_a1")
        self.gridLayout.addWidget(self.SpinBox_a1, 0, 5, 1, 1)
        self.Slider_a1 = QtWidgets.QSlider(self.centralWidget)
        self.Slider_a1.setMinimum(1)
        self.Slider_a1.setMaximum(100)
        self.Slider_a1.setProperty("value", 10)
        self.Slider_a1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_a1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_a1.setTickInterval(10)
        self.Slider_a1.setObjectName("Slider_a1")
        self.gridLayout.addWidget(self.Slider_a1, 1, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mplwidget_integral = MPL_WIDGET_2D(self.tab)
        self.mplwidget_integral.setObjectName("mplwidget_integral")
        self.horizontalLayout_3.addWidget(self.mplwidget_integral)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.SpinBox_P1 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.SpinBox_P1.setEnabled(True)
        self.SpinBox_P1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_P1.setKeyboardTracking(False)
        self.SpinBox_P1.setDecimals(3)
        self.SpinBox_P1.setMaximum(5.0)
        self.SpinBox_P1.setSingleStep(0.01)
        self.SpinBox_P1.setProperty("value", 0.75)
        self.SpinBox_P1.setObjectName("SpinBox_P1")
        self.horizontalLayout.addWidget(self.SpinBox_P1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.SpinBox_P2 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.SpinBox_P2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_P2.setKeyboardTracking(False)
        self.SpinBox_P2.setDecimals(3)
        self.SpinBox_P2.setMinimum(-5.0)
        self.SpinBox_P2.setMaximum(0.0)
        self.SpinBox_P2.setSingleStep(0.01)
        self.SpinBox_P2.setProperty("value", -0.75)
        self.SpinBox_P2.setObjectName("SpinBox_P2")
        self.horizontalLayout.addWidget(self.SpinBox_P2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Button_reset = QtWidgets.QPushButton(self.tab_2)
        self.Button_reset.setObjectName("Button_reset")
        self.horizontalLayout.addWidget(self.Button_reset)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.mplwidget_spiral = MPL_WIDGET_2D(self.tab_2)
        self.mplwidget_spiral.setMinimumSize(QtCore.QSize(0, 0))
        self.mplwidget_spiral.setObjectName("mplwidget_spiral")
        self.verticalLayout_2.addWidget(self.mplwidget_spiral)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fresnel"))
        self.label_2.setText(_translate("MainWindow", "a (screen width)  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Integral"))
        self.label.setText(_translate("MainWindow", "P1"))
        self.label_3.setText(_translate("MainWindow", "P2"))
        self.pushButton.setText(_translate("MainWindow", "Move"))
        self.Button_reset.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Spiral"))

from mplwidget import MPL_WIDGET_2D
