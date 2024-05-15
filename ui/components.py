from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QCursor, QMouseEvent, QTextLayout, QPainter
from PyQt5.QtWidgets import QTextBrowser, QPlainTextEdit

from utils.config_utils import Conf


class MyQPlainTextEdit(QPlainTextEdit):

    def __init__(self, conf):
        super().__init__()
        self.is_mover = False
        self.m_pos = None
        self.file_tell = 0
        self.scroll_value = 0
        self.conf = conf
        self.setStyleSheet('border: none;')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_mover = True
            self.m_pos = event.globalPos() - self.parent().pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_mover:
            self.parent().move(event.globalPos() - self.m_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_mover = False

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - 1)
        else:
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + 1)
        print(self.verticalScrollBar().value())
