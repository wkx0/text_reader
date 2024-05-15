from PyQt5 import QtCore
from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QMessageBox

from ui.setting_ui import SettingUI


class SettingEvent(SettingUI):

    def __init__(self):
        super().__init__()
        self.load_config()
        QMetaObject.connectSlotsByName(self)  # 自动自动连接信号和槽

    @QtCore.pyqtSlot()
    def on_select_file_button_clicked(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt)",
                                                   options=options)

        if file_path:
            self.file_Edit.setText(file_path)

    @QtCore.pyqtSlot()
    def on_select_font_color_button_clicked(self):
        color_dialog = QColorDialog(self)
        color_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        color = color_dialog.getColor()

        if color.isValid():
            color_name = color.name()
            self.font_color_Edit.setText(color_name)

    @QtCore.pyqtSlot()
    def on_select_background_color_button_clicked(self):
        color_dialog = QColorDialog(self)
        color_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        color = color_dialog.getColor()

        if color.isValid():
            color_name = color.name()
            self.background_color_Edit.setText(color_name)

    @QtCore.pyqtSlot()
    def on_save_button_clicked(self):
        self.conf.set_text_path(self.file_Edit.text())
        self.conf.set_line_height(self.line_height_Edit.text())
        self.conf.set_font_size(self.font_size_Edit.text())
        self.conf.set_font_color(self.font_color_Edit.text())
        self.conf.set_background_color(self.background_color_Edit.text())
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("保存成功！")
        msg.setWindowTitle("成功")
        msg.show()

    @QtCore.pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    def load_config(self):
        if self.conf.text_path != "":
            self.file_Edit.setText(self.conf.text_path)
        if self.conf.line_height != "":
            self.line_height_Edit.setValue(int(self.conf.line_height))
        if self.conf.font_size != "":
            self.font_size_Edit.setValue(int(self.conf.font_size))
        if self.conf.font_color != "":
            self.font_color_Edit.setText(self.conf.font_color)
        if self.conf.background_color != "":
            self.background_color_Edit.setText(self.conf.background_color)
