# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(400, 100, 300, 200)
window.setWindowTitle('My first app')

window.show()
sys.exit(app.exec_())
