import sys

from random import randint
from PyQt6 import uic
from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFormLayout


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.label = QLabel()
        canvas = QPixmap(1000, 1000)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label)


    def run(self):
        x, y, r = randint(1, 1000), randint(1, 901), randint(10, 400)
        print(x, y)
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        painter.setBrush(Qt.GlobalColor.yellow)
        painter.drawEllipse(QRectF(x, y, r, r))
        painter.end()
        self.label.setPixmap(canvas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
