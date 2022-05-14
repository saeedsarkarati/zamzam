import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
# Subclass QMainWindow to customize your application's main window
app = QApplication(sys.argv)
window = QMainWindow()
# ~ window.setFixedSize(QSize(400, 300))
window.setGeometry(190,100,400,400)
window.setWindowTitle("My App")
b = []
nb = 3
for i in range (nb):
	b.append (QPushButton( parent = window))
	b[i].setText (str(i) )
	b[i].setGeometry(100 + i * 50,100,40,40)

window.show()
app.exec()
