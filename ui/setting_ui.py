# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QSpinBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSpacerItem, QSizePolicy, QComboBox

from utils.config_utils import Conf


class SettingUI(QWidget):

    def __init__(self):
        super().__init__()

        # 防止主窗口跟随子窗口一起关闭
        # self.setWindowFlag(QtCore.Qt.Window)

        self.file_label = QLabel("文件：")
        self.encoding_label = QLabel("编码方式：")
        self.line_height_label = QLabel("行高：")
        self.font_size_label = QLabel("字体大小：")
        self.font_color_label = QLabel("字体颜色：")
        self.background_color_label = QLabel("背景颜色：")
        self.find_label = QLabel("查找：")

        self.file_Edit = QLineEdit()
        self.file_Edit.setObjectName("file_Edit")

        self.encoding_Box = QComboBox()
        self.encoding_Box.addItem("utf-8")
        self.encoding_Box.addItem("gbk")
        self.encoding_Box.setObjectName("encoding_Box")

        self.line_height_Edit = QSpinBox()
        self.line_height_Edit.setObjectName("line_height_Edit")
        self.font_size_Edit = QSpinBox()
        self.font_size_Edit.setObjectName("font_size_Edit")
        self.font_color_Edit = QLineEdit()
        self.font_color_Edit.setObjectName("font_color_Edit")
        self.background_color_Edit = QLineEdit()
        self.background_color_Edit.setObjectName("background_color_Edit")
        self.find_Edit = QLineEdit()
        self.find_Edit.setObjectName("find_Edit")

        self.select_file_button = QPushButton("选择文件")
        self.select_file_button.setObjectName("select_file_button")
        self.select_font_color_button = QPushButton("选择颜色")
        self.select_font_color_button.setObjectName("select_font_color_button")
        self.select_background_color_button = QPushButton("选择颜色")
        self.select_background_color_button.setObjectName("select_background_color_button")
        self.save_button = QPushButton("保存")
        self.save_button.setObjectName("save_button")
        self.find_next_button = QPushButton("下一个")
        self.find_next_button.setObjectName("find_next_button")
        self.find_up_button = QPushButton("上一个")
        self.find_up_button.setObjectName("find_up_button")
        self.close_button = QPushButton("取消")
        self.close_button.setObjectName("close_button")

        # 水平布局
        h_box = QHBoxLayout()
        vbox = QVBoxLayout()

        h_box.addWidget(self.file_label)
        h_box.addWidget(self.file_Edit)
        h_box.addWidget(self.select_file_button)

        # 添加到垂直布局
        vbox.addLayout(h_box)
        vbox.addStretch(1)

        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.encoding_label)
        h_box1.addWidget(self.encoding_Box)
        h_box1.addStretch(1)

        vbox.addLayout(h_box1)
        vbox.addStretch(1)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.line_height_label)
        h_box2.addWidget(self.line_height_Edit)
        h_box2.addStretch(1)
        vbox.addLayout(h_box2)
        vbox.addStretch(1)

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.font_size_label)
        h_box3.addWidget(self.font_size_Edit)
        h_box3.addStretch(1)

        vbox.addLayout(h_box3)
        vbox.addStretch(1)

        h_box4 = QHBoxLayout()
        h_box4.addWidget(self.font_color_label)
        h_box4.addWidget(self.font_color_Edit)
        h_box4.addWidget(self.select_font_color_button)
        vbox.addLayout(h_box4)
        vbox.addStretch(1)

        h_box5 = QHBoxLayout()
        h_box5.addWidget(self.background_color_label)
        h_box5.addWidget(self.background_color_Edit)
        h_box5.addWidget(self.select_background_color_button)

        vbox.addLayout(h_box5)
        vbox.addStretch(1)

        h_box6 = QHBoxLayout()
        h_box6.addWidget(self.find_label)
        h_box6.addWidget(self.find_Edit)
        h_box6.addWidget(self.find_next_button)
        h_box6.addWidget(self.find_up_button)

        vbox.addLayout(h_box6)
        vbox.addStretch(3)

        h_box6 = QHBoxLayout()
        h_box6.addWidget(self.save_button)
        h_box6.addWidget(self.close_button)
        vbox.addLayout(h_box6)

        vbox.addStretch(1)

        self.setLayout(vbox)

        # 获取屏幕的宽高 设置窗口居中
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        w = screen_size.width() / 2
        h = screen_size.height() / 2

        # 设置窗口样式
        self.setGeometry(w, h, 400, 300)  # 设置初始位置与窗口大小
        self.setWindowTitle("设置")
        self.setMinimumSize(100, 25)
