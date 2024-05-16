from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QCursor, QMouseEvent, QTextLayout, QPainter
from PyQt5.QtWidgets import QTextBrowser, QPlainTextEdit

from utils.config_utils import Conf


class MyQPlainTextEdit(QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # 启用鼠标跟踪功能

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - 1)
        else:
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + 1)
