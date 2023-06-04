import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 对话框是人机交互中最常用的一种方式。PyQt5中使用QDialog来表示对话框，它有几个常用的子类，QMessageBox、QFileDialog、QInputDialog、QFontDialog。

# QMessageBox 跳一个窗口  选择是或否  弹出消息对话框，也是最常用的对话框

class DialogDemo(QMainWindow):
    
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("QMessageBox demo")
        self.resize(600, 400)
        
        self.button = QPushButton(self)
        self.button.setText("点击弹出QMessageBox")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)
    
    def showDialog(self):
        # warning、critical、question
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)  # QMessageBox
        print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogDemo()
    demo.show()
    sys.exit(app.exec_())