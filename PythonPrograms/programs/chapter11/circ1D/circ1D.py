# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from Ui_circ1D import Ui_MainWindow
from numpy import pi, linspace
import scipy.special as ss

class Circular(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fig1()
    def fig1(self):
        lamda=self.slider_lambda.value()*1.E-9; k=(2.*pi)/lamda  #wavelength of light in vaccuum
        
        a=self.slider_a.value()*1.E-6  #radius of the circular aperture (m)
        f_2 = self.slider_f2.value()     # f2 is the focal length of the lens L2 (m)
        e= self.slider_e.value() * 1.E-3  # Side of a square-shaped screen (m)
        X_Mmax=e/2. ; X_Mmin = -e/2.
        Y_Mmax=X_Mmax ; Y_Mmin =  X_Mmin
        N =800
        X=linspace(X_Mmin, X_Mmax,N); Y=X # coordinates of screen
        #1D representation
        q=X # intermediate variable
        beta=k*a*q/f_2
        dx=1.22*lamda*f_2/a*1.E2
        self.lineEdit_dx.setText(str("%.4f" %dx))
        I=(2*ss.jv(1,beta)/beta)**2
        # figure 1 D
        mpl1d=self.mplwidget1D.canvas
        mpl1d.ax.clear()
        mpl1d.ax.plot(X,I, color='k', linewidth=2)
        mpl1d.ax.set_xlim(X_Mmin, X_Mmax)
        mpl1d.ax.set_xlabel(r'$X (m)$',fontsize=12, fontweight='bold')
        mpl1d.ax.set_ylabel(r'$I(X,Y)/I_0$',fontsize=12, fontweight='bold')
        mpl1d.figure.suptitle('Fraunhofer Circular Diffraction',fontsize=14, fontweight='bold')
        mpl1d.ax.set_title(r"$\lambda = %.3e \ m, \ a = %.2e \ m, \ f_2 = %.1f \ m$"% (lamda,a, f_2),fontsize=10)
        mpl1d.draw()

    @pyqtSlot("int")   
    def on_slider_lambda_valueChanged(self, value):
        self.SpinBox_lambda.setValue(value)
        self.fig1()
    @pyqtSlot("int")
    def on_slider_a_valueChanged(self, value):
        self.SpinBox_a.setValue(value)
        self.fig1()
    @pyqtSlot("int")
    def on_slider_e_valueChanged(self, value):
        self.SpinBox_e.setValue(value)
        self.fig1()
    @pyqtSlot("int")
    def on_slider_f2_valueChanged(self, value):
        self.SpinBox_f2.setValue(value)
        self.fig1()
    @pyqtSlot("int")
    def on_SpinBox_lambda_valueChanged(self, value):
        self.slider_lambda.setValue(value)
    
    @pyqtSlot("double")
    def on_SpinBox_a_valueChanged(self, value):
        self.slider_a.setValue(value)
    @pyqtSlot("double")
    def on_SpinBox_e_valueChanged(self, value):
        self.slider_e.setValue(value)
    @pyqtSlot("double")
    def on_SpinBox_f2_valueChanged(self, value):

        self.slider_f2.setValue(value)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    MyApplication = Circular()
    MyApplication.show()
    sys.exit(app.exec_())
