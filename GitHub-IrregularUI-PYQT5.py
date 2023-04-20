from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
import sys


class Actions(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):

        # setflags necessary for irregular shape of window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # get image
        pixmap = QPixmap("page to image .png")

        # resize window to image size
        self.resize(pixmap.width(), pixmap.height())

        # add label to size of window and add image to it, resizing to same size as window/image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(pixmap)
        self.background_image.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # pushbutton just added just cause
        self.button = QPushButton(self)
        self.button.setText("This is a test!")
        self.button.adjustSize()
        self.button.move(100, 100)

        self.show()


    # mouse events for moving irregular shaped window that doens't have a toolbar
    def mousePressEvent(self, event):

        # get position of mouse press, which will be used in the mousemove event function
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        # if the press click is in the upper part of the UI and it's a mousemove event, then move UI
        # 40 pixel height is what i set the area at top of UI to be clickable to move the UI around, feel
        # free to change it
        if self.x() < self.oldPos.x() < (self.x() + self.width()) and self.y() < self.oldPos.y() < (self.y() + 40):

            # difference between global position and old position for calculation how to move UI
            delta = QPoint(event.globalPos() - self.oldPos)

            # move UI to new location
            self.move(self.x() + delta.x(), self.y() + delta.y())

            # reset variable so that UI moves as mouse is held down
            self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Actions()
    sys.exit(app.exec_())
