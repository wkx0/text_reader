# -*- coding: utf-8 -*-


from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                         QFont, QFontDatabase, QGradient, QIcon,
                         QImage, QKeySequence, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QTextEdit,
                             QWidget, QMainWindow, QTextBrowser, QScrollArea, QAction, QMenu, QSystemTrayIcon,
                             QPushButton)

from ui.components import MyQPlainTextEdit
from utils.config_utils import Conf


class TextUI(QWidget):
    confPath = r"./conf/Config.conf"

    def __init__(self):
        super().__init__()
        self.conf = Conf(self.confPath)
        self.show_style = ""
        self.hide_style = ""

        # 文本编辑框
        self.plain_text = MyQPlainTextEdit()
        self.plain_text.setReadOnly(True)
        # 任务栏图标不显示
        self.plain_text.setTextInteractionFlags(Qt.NoTextInteraction)

        # 隐藏垂直滚动条
        self.plain_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 隐藏水平滚动条
        self.plain_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        h_box = QHBoxLayout()
        h_box.addWidget(self.plain_text)

        # 无边框
        h_box.setContentsMargins(0, 0, 0, 0)
        self.setLayout(h_box)

        x = 200
        y = 200
        h = 400
        w = 700
        if self.conf.win_x:
            x = int(self.conf.win_x)
        if self.conf.win_y:
            y = int(self.conf.win_y)

        if self.conf.win_h:
            h = int(self.conf.win_h)
        if self.conf.win_w:
            w = int(self.conf.win_w)

        # 设置窗口样式
        self.setGeometry(x, y, w, h)  # 设置初始位置与窗口大小
        self.setMinimumSize(100, 25)
        self.setWindowOpacity(0.5)  # 设置窗口透明度
        self.setWindowTitle("text reader")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 设置窗口无边框
        self.plain_text.setStyleSheet(self.generate_style())

    def generate_style(self, font_color=None, font_size=None, line_height=None, background_color=None):
        """
        生成样式
        :return:
        """
        font_color = font_color if font_color is not None else self.conf.font_color
        font_size = font_size if font_size is not None else self.conf.font_size
        line_height = line_height if line_height is not None else self.conf.line_height
        background_color = background_color if background_color is not None else self.conf.background_color
        if font_color == "":
            font_color = "white"
            self.conf.set_font_color("white")
        if font_size == "":
            font_size = 14
            self.conf.set_font_size(font_size)
        if line_height == "":
            line_height = 14
            self.conf.set_line_height(line_height)
        if background_color == "":
            background_color = "#808080"
            self.conf.set_background_color(background_color)

        self.hide_style = f"""
            QPlainTextEdit {{
                color: rgba(0,0,0,0);
                border: none;
                font-size: {font_size}px;
                line-height: {line_height}px;
                background-color: {background_color};
            }}
        """
        self.show_style = f"""
            QPlainTextEdit {{
                color: {font_color};
                border: none;
                font-size: {font_size}px;
                line-height: {line_height}px;
                background-color: {background_color};
            }}
        """
        return self.show_style
