from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor

class Node(QRect):
    def __init__(self, begin, destination, name):
        super().__init__( begin, destination)
        self.name = name


    def show(self):
        # print("Hello World from anothe file :)")
        print(self.name)

    def getName(self):
        return self.name
    def contains(self, point):
        return self.rect().contains(point)
    
