from Control_Panel import MyGUI
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MyGUI()
    window.setWindowTitle("Graph Algorithms Visualizer")
    with open('style.qss', 'r') as f1, open('style2.qss', 'r') as f2, open('QPushButton.qss', 'r') as f3:
        style1 = f1.read()
        style2 = f2.read()
        button = f3.read()
        window.setStyleSheet(style1  +  button)
    
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')