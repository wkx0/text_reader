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
        self.font_color = "white"
        # 文本编辑框
        self.plain_text = MyQPlainTextEdit(self.conf)
        self.plain_text.setReadOnly(True)

        # 隐藏垂直滚动条
        self.plain_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # # 隐藏水平滚动条
        self.plain_text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        h_box = QHBoxLayout()
        self.bt = QPushButton("test")
        h_box.addWidget(self.plain_text)
        # h_box.addWidget(self.bt)
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
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setWindowTitle("text reader")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置窗口始终在顶部显示
        self.setStyleSheet('border: none;')
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 设置窗口无边框
        self.load_config()

    def load_config(self):
        if self.conf.line_height != "":
            self.plain_text.setStyleSheet("QPlainTextEdit {line-height: " + self.conf.line_height + "px;border: none;}")
        else:
            self.conf.set_line_height(10)
            self.plain_text.setStyleSheet("QPlainTextEdit {line-height: 10px;border: none;}")

        # if self.conf.font_size != "":
        #     self.plain_text.setFont(QFont("Arial", int(self.conf.font_size)))
        # else:
        #     self.conf.set_font_size(10)
        #     self.plain_text.setFont(QFont("Arial", 10))
        # if self.conf.font_color != "":
        #     self.plain_text.setStyleSheet(f"color: {self.conf.font_color};")  # 设置字体颜色
        #     self.font_color = self.conf.font_color
        # else:
        #     self.plain_text.setStyleSheet("color: white;")  # 设置字体颜色
        #     self.conf.set_font_color("white")
        #
        if self.conf.background_color != "":
            self.setStyleSheet(f'background-color: {self.conf.background_color};')
        else:
            self.conf.set_background_color("#808080")
            self.setStyleSheet(f'background-color: #808080;')
