# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PrismaticSlab.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 646)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.SpinBox_Lambda3 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda3.setSuffix("")
        self.SpinBox_Lambda3.setDecimals(1)
        self.SpinBox_Lambda3.setMinimum(625.0)
        self.SpinBox_Lambda3.setMaximum(800.0)
        self.SpinBox_Lambda3.setSingleStep(0.1)
        self.SpinBox_Lambda3.setProperty("value", 660.0)
        self.SpinBox_Lambda3.setObjectName("SpinBox_Lambda3")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda3, 2, 4, 1, 1)
        self.label_Lambda2 = QtWidgets.QLabel(self.centralWidget)
        self.label_Lambda2.setObjectName("label_Lambda2")
        self.gridLayout_2.addWidget(self.label_Lambda2, 1, 3, 1, 1)
        self.SpinBox_Lambda1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda1.setDecimals(1)
        self.SpinBox_Lambda1.setMinimum(300.0)
        self.SpinBox_Lambda1.setMaximum(519.0)
        self.SpinBox_Lambda1.setSingleStep(0.1)
        self.SpinBox_Lambda1.setProperty("value", 400.0)
        self.SpinBox_Lambda1.setObjectName("SpinBox_Lambda1")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda1, 0, 4, 1, 1)
        self.label_Lambda1 = QtWidgets.QLabel(self.centralWidget)
        self.label_Lambda1.setObjectName("label_Lambda1")
        self.gridLayout_2.addWidget(self.label_Lambda1, 0, 3, 1, 1)
        self.label_Lambda3 = QtWidgets.QLabel(self.centralWidget)
        self.label_Lambda3.setObjectName("label_Lambda3")
        self.gridLayout_2.addWidget(self.label_Lambda3, 2, 3, 1, 1)
        self.cbg = QtWidgets.QCheckBox(self.centralWidget)
        self.cbg.setChecked(True)
        self.cbg.setObjectName("cbg")
        self.gridLayout_2.addWidget(self.cbg, 1, 5, 1, 1)
        self.pushButton_Lambda1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Lambda1.setObjectName("pushButton_Lambda1")
        self.gridLayout_2.addWidget(self.pushButton_Lambda1, 0, 6, 1, 1)
        self.SpinBox_Lambda2 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_Lambda2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_Lambda2.setDecimals(1)
        self.SpinBox_Lambda2.setMinimum(520.0)
        self.SpinBox_Lambda2.setMaximum(580.0)
        self.SpinBox_Lambda2.setSingleStep(0.1)
        self.SpinBox_Lambda2.setProperty("value", 530.0)
        self.SpinBox_Lambda2.setObjectName("SpinBox_Lambda2")
        self.gridLayout_2.addWidget(self.SpinBox_Lambda2, 1, 4, 1, 1)
        self.pushButton_Lambda123 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Lambda123.setObjectName("pushButton_Lambda123")
        self.gridLayout_2.addWidget(self.pushButton_Lambda123, 3, 6, 1, 1)
        self.cbb = QtWidgets.QCheckBox(self.centralWidget)
        self.cbb.setChecked(True)
        self.cbb.setObjectName("cbb")
        self.gridLayout_2.addWidget(self.cbb, 0, 5, 1, 1)
        self.SpinBox_angle = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_angle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_angle.setSuffix("")
        self.SpinBox_angle.setDecimals(2)
        self.SpinBox_angle.setMinimum(0.0)
        self.SpinBox_angle.setMaximum(50.0)
        self.SpinBox_angle.setSingleStep(0.1)
        self.SpinBox_angle.setProperty("value", 1.0)
        self.SpinBox_angle.setObjectName("SpinBox_angle")
        self.gridLayout_2.addWidget(self.SpinBox_angle, 1, 2, 1, 1)
        self.SpinBox_ndx = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.SpinBox_ndx.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.SpinBox_ndx.setSuffix("")
        self.SpinBox_ndx.setDecimals(2)
        self.SpinBox_ndx.setMaximum(20.0)
        self.SpinBox_ndx.setSingleStep(0.1)
        self.SpinBox_ndx.setProperty("value", 1.5)
        self.SpinBox_ndx.setObjectName("SpinBox_ndx")
        self.gridLayout_2.addWidget(self.SpinBox_ndx, 0, 2, 1, 1)
        self.label_ndx = QtWidgets.QLabel(self.centralWidget)
        self.label_ndx.setObjectName("label_ndx")
        self.gridLayout_2.addWidget(self.label_ndx, 0, 1, 1, 1)
        self.label_angle = QtWidgets.QLabel(self.centralWidget)
        self.label_angle.setObjectName("label_angle")
        self.gridLayout_2.addWidget(self.label_angle, 1, 1, 1, 1)
        self.cbr = QtWidgets.QCheckBox(self.centralWidget)
        self.cbr.setChecked(True)
        self.cbr.setAutoRepeat(False)
        self.cbr.setAutoExclusive(False)
        self.cbr.setObjectName("cbr")
        self.gridLayout_2.addWidget(self.cbr, 2, 5, 1, 1)
        self.pushButton_Lambda2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Lambda2.setObjectName("pushButton_Lambda2")
        self.gridLayout_2.addWidget(self.pushButton_Lambda2, 1, 6, 1, 1)
        self.pushButton_Lambda3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_Lambda3.setObjectName("pushButton_Lambda3")
        self.gridLayout_2.addWidget(self.pushButton_Lambda3, 2, 6, 1, 1)
        self.cbPhi = QtWidgets.QCheckBox(self.centralWidget)
        self.cbPhi.setEnabled(True)
        self.cbPhi.setChecked(True)
        self.cbPhi.setObjectName("cbPhi")
        self.gridLayout_2.addWidget(self.cbPhi, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplwidget = MPL_WIDGET_2D(self.centralWidget)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout.addWidget(self.mplwidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prismatic Slab"))
        self.label_Lambda2.setText(_translate("MainWindow", "Wavelength Green (nm)"))
        self.label_Lambda1.setText(_translate("MainWindow", "Wavelength Blue (nm)"))
        self.label_Lambda3.setText(_translate("MainWindow", "Wavelength Red (nm)"))
        self.cbg.setText(_translate("MainWindow", "View Green"))
        self.pushButton_Lambda1.setText(_translate("MainWindow", "Blue light"))
        self.pushButton_Lambda123.setText(_translate("MainWindow", "Wight light"))
        self.cbb.setText(_translate("MainWindow", "View Blue"))
        self.label_ndx.setText(_translate("MainWindow", "Slab index n"))
        self.label_angle.setText(_translate("MainWindow", "Corner angle (mrad)"))
        self.cbr.setText(_translate("MainWindow", "View Red"))
        self.pushButton_Lambda2.setText(_translate("MainWindow", "Green light"))
        self.pushButton_Lambda3.setText(_translate("MainWindow", "Red light"))
        self.cbPhi.setText(_translate("MainWindow", "Phase shift pi (Reflection)"))

from mplwidget import MPL_WIDGET_2D