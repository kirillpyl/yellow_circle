import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        self.x = 0
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.x != 0:
            self.dr(qp)
        qp.end()

    def dr(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        t = randint(1, 200)
        qp.drawEllipse(230, 130, t, t)

    def run(self):
        self.x = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())