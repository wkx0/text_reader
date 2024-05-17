from PyQt5.QtCore import pyqtSignal, Qt, QRect, QMetaObject, QEvent, QTimer, QCoreApplication, QUrl, QFile, QIODevice, \
    QTextStream
from PyQt5.QtGui import QEnterEvent, QIcon, QGuiApplication, QTextDocument
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMessageBox

from ui.text_ui import TextUI
from windows.setting_windows import SettingWin
from public import logo_ico


class TextEvent(TextUI):
    # LogSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.cur_file = ""
        self.cur_encoding = "utf-8"
        self.tray_icon = None  # 托盘图标
        self.setting_win = SettingWin(self.conf)  # 设置窗口
        self.is_show_setting_win = False  # 是否显示设置窗口
        self.is_mover = False
        self.m_pos = None
        self.is_resize = True  # 是否调整大小

        self.direction = None  # 调整方向
        self.right_edge = None  # 右边缘
        self.bottom_edge = None  # 下边缘
        self.right_bottom_edge = None  # 右下边缘
        self.top_edge = None  # 上边缘
        self.is_mover = False  # 是否移动
        self.m_pos = None  # 鼠标位置
        self.is_show = False  # 是否显示

        self.create_menu()
        self.setMouseTracking(True)  # 启用鼠标跟踪功能
        self.installEventFilter(self)  # 安装事件过滤器
        QMetaObject.connectSlotsByName(self)  # 自动自动连接信号和槽
        self.plain_text.verticalScrollBar().setPageStep(1)
        self.plain_text.verticalScrollBar().valueChanged.connect(self.scroll_value_changed)
        self.setting_win.signal.connect(self.update_ui)
        self.setting_win.close_signal.connect(self.setting_win_close)
        self.setting_win.find_signal.connect(self.find_text)

    def mousePressEvent(self, event):
        """
        鼠标点击事件
        :param event:
        :return:
        """
        if event.button() == Qt.LeftButton:
            if self.is_resize:
                # 鼠标左键点击下边界区域 调整大小
                if self.direction == 'bottom':
                    self.windowHandle().startSystemResize(Qt.BottomEdge)
                # 鼠标左键点击右边界区域 调整大小
                elif self.direction == 'right':
                    self.windowHandle().startSystemResize(Qt.RightEdge)
                elif self.direction == 'right_bottom':
                    self.windowHandle().startSystemResize(Qt.RightEdge | Qt.BottomEdge)
                elif self.direction == 'top':
                    self.windowHandle().startSystemResize(Qt.TopEdge)
            else:
                self.is_mover = True
                self.m_pos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        """
        鼠标移动事件
        :param event:
        :return:
        """
        self.right_edge = QRect(self.width() - 10, 0, self.width(), self.height())
        self.bottom_edge = QRect(0, self.height() - 10, self.width() - 25, self.height())
        self.right_bottom_edge = QRect(self.width() - 25, self.height() - 10, self.width(), self.height())
        self.top_edge = QRect(0, 0, self.width(), 10)
        # 根据鼠标在窗口的位置 改变鼠标手势
        if not self.isMaximized():
            if self.is_mover:
                self.move(event.globalPos() - self.m_pos)
            elif self.bottom_edge.contains(event.pos()):
                self.plain_text.viewport().setCursor(Qt.SizeVerCursor)
                self.direction = "bottom"
                self.is_resize = True
            elif self.right_edge.contains(event.pos()):
                self.plain_text.viewport().setCursor(Qt.SizeHorCursor)
                self.direction = "right"
                self.is_resize = True
            elif self.right_bottom_edge.contains(event.pos()):
                self.plain_text.viewport().setCursor(Qt.SizeFDiagCursor)
                self.direction = "right_bottom"
                self.is_resize = True
            elif self.top_edge.contains(event.pos()):
                self.plain_text.viewport().setCursor(Qt.SizeVerCursor)
                self.direction = "top"
                self.is_resize = True
            else:
                self.plain_text.viewport().setCursor(Qt.ArrowCursor)
                self.direction = None
                self.is_resize = False

    def mouseReleaseEvent(self, event):
        self.is_mover = False

    def leaveEvent(self, event):
        self.is_show = False
        QGuiApplication.restoreOverrideCursor()
        if not self.is_show_setting_win:
            self.plain_text.setStyleSheet(self.hide_style)  # 设置文本颜色为透明

    def enterEvent(self, event):
        self.plain_text.setStyleSheet(self.show_style)

    def eventFilter(self, obj, event):
        """
        事件过滤器, 鼠标进入其它控件后还原为标准鼠标样式, 方向属性变为None
        :param obj:
        :param event:
        :return:
        """
        if event.type() == QEvent.KeyPress:
            modifiers = event.modifiers()
            if modifiers & Qt.AltModifier:
                self.is_show = True
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
            self.direction = None

        return super().eventFilter(obj, event)

    def showEvent(self, event):
        """
        窗口显示事件
        :param event:
        :return:
        """
        if self.conf.text_encoding is None:
            self.cur_encoding = "utf-8"
            self.conf.set_text_encoding("utf-8")
        text = self.load_text()
        self.plain_text.setPlainText(text)
        if text != "" and self.conf.line is not None:
            cursor = self.plain_text.textCursor()
            cursor.movePosition(cursor.Start)  # 将光标移动到文本开头
            for _ in range(int(self.conf.line) + self.plain_text.verticalScrollBar().pageStep()):  # 移动光标到指定行之前
                cursor.movePosition(cursor.Down)
            self.plain_text.setTextCursor(cursor)  # 将光标移动到指定行

    def resizeEvent(self, event):
        """
        窗口调整大小事件
        :param event:
        :return:
        """
        new_size = event.size()
        self.conf.set_win_w(new_size.width())
        self.conf.set_win_h(new_size.height())

    def moveEvent(self, event):
        self.conf.set_win_x(event.pos().x())
        self.conf.set_win_y(event.pos().y())

    def update_ui(self, file, encoding, line_height, font_size, font_color, background_color):
        if file != self.cur_file or encoding != self.cur_encoding:
            self.cur_file = file
            self.cur_encoding = encoding
            text = self.load_text()
            self.plain_text.setPlainText(text)
        self.plain_text.setStyleSheet(self.generate_style(font_color, font_size, line_height, background_color))

    def setting_win_close(self):
        self.is_show_setting_win = False
        cursor = self.plain_text.textCursor()
        cursor.clearSelection()
        self.plain_text.setTextCursor(cursor)

    def scroll_value_changed(self):
        """
        滚动条值改变事件
        :return:
        """
        self.conf.set_line(self.plain_text.verticalScrollBar().value())

    def open_setting_win(self):
        self.plain_text.setStyleSheet(self.show_style)
        self.setting_win.show()
        self.is_show_setting_win = True

    def find_text(self, text, direction):
        flag = QTextDocument.FindFlags()
        if direction == "reverse":
            flag = QTextDocument.FindBackward
        find = self.plain_text.find(text, flag)
        if not find:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("找不到了！")
            msg.setWindowTitle("成功")
            msg.show()

    def create_menu(self):
        """
        创建菜单
        :return:
        """
        tray_menu = QMenu()
        # 添加菜单项到菜单
        tray_menu.addAction("设置", self.open_setting_win)
        tray_menu.addAction("退出", self.quit_app)

        # 创建托盘图标菜单
        self.tray_icon = QSystemTrayIcon()

        # 将菜单设置到托盘图标
        self.tray_icon.setContextMenu(tray_menu)

        # 设置托盘图标的默认图标
        default_icon = QIcon(QIcon(':/logo.ico'))
        self.tray_icon.setIcon(default_icon)

        # 设置托盘图标的鼠标提示
        self.tray_icon.setToolTip("这是一个摸鱼神器")

        # 在系统托盘中显示图标
        self.tray_icon.show()

    def load_text(self, encoding=None):
        text = ""
        if self.conf.text_path is not None:
            self.cur_file = self.conf.text_path
        if encoding is not None:
            self.cur_encoding = encoding

        try:
            file = QFile(self.cur_file)
            if file.open(QIODevice.ReadOnly | QIODevice.Text):
                stream = QTextStream(file)
                stream.setCodec(self.cur_encoding)
                text = stream.readAll()
        except Exception as e:
            print(e)

        return text

    @staticmethod
    def quit_app():
        QCoreApplication.quit()
