from PyQt5 import QtWidgets
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import time
from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtGui import QBrush
import sys
import os 

class Main_Class (QMainWindow):
    def __init__(self):
        # Initilizes the attributes of the Main_Class
        super(Main_Class, self).__init__()
        self.setGeometry(800, 400, 1200, 600)
        # Setting stylesheets and the geom
        # etry of the original window, the stylesheet aka 
        # inline css is inherited by all the objects with the self parameter unless otherwise specified
        self.setStyleSheet(
            "background: #FFFFFF;font-family: Comic Sans MS, cursive, sans-serif;font-size: 25px;letter-spacing: 2px;")
        self.setWindowTitle("Sorting Visualizer")

    def initUI(self):
        # Self parameter inherits properties from the class
        self.title=QtWidgets.QLabel(self)
        # Defining "self.title" as PyQt label module
        self.title.setText("Sorting Visualizer ")
        self.title.setGeometry(00,00,400,60)
        
    def paintEvent (self,lst):
        lst=[[1, 3, 5, 2, 32, 45, 24, 324]]
        painter=QPainter(self)
        for j in lst:
            time.sleep(0.1)
            for e,i in enumerate(j):
                painter.drawRect((50+(e*20)),(-10),20,(i*10))
                
                
                
def change(lst):
    pass
            
        

            
            
# window function tells the system the parameters to use
def window():
    app = QApplication(sys.argv)
    win = Main_Class()
    win.show( )
    sys.exit(app.exec())
# Calling the function 
window() 


def bubble_sort(data):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print (data)




# data=[1,3,5,45,2,32,24,324]
# bubble_sort(data)
