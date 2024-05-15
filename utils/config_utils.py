from configparser import ConfigParser
import os


class Conf:
    def __init__(self, path):
        self.path = path
        self.create_config()
        self.config = ConfigParser()
        self.config.read(self.path, encoding="utf-8")

    @property
    def line(self):
        return self.get_option("text", "line")

    def set_line(self, value):
        self.set_option("text", "line", str(value))

    @property
    def line_height(self):
        return self.get_option("text", "line_height")

    def set_line_height(self, value):
        self.set_option("text", "line_height", str(value))

    @property
    def win_x(self):
        return self.get_option("win", "x")

    def set_win_x(self, value):
        self.set_option("win", "x", str(value))

    @property
    def win_y(self):
        return self.get_option("win", "y")

    def set_win_y(self, value):
        self.set_option("win", "y", str(value))

    @property
    def win_h(self):
        return self.get_option("win", "h")

    def set_win_h(self, value):
        self.set_option("win", "h", str(value))

    @property
    def win_w(self):
        return self.get_option("win", "w")

    def set_win_w(self, value):
        self.set_option("win", "w", str(value))

    @property
    def text_path(self):
        return self.get_option("text", "path")

    def set_text_path(self, value):
        self.set_option("text", "path", str(value))

    @property
    def font_size(self):
        return self.get_option("text", "font_size")

    def set_font_size(self, value):
        self.set_option("text", "font_size", str(value))

    @property
    def font_color(self):
        return self.get_option("text", "font_color")

    def set_font_color(self, value):
        self.set_option("text", "font_color", str(value))

    @property
    def background_color(self):
        return self.get_option("text", "background_color")

    def set_background_color(self, value):
        self.set_option("text", "background_color", str(value))

    def get_option(self, section, option):
        if self.section_and_option_is(section, option):
            value = self.config.get(section, option)
            return value
        else:
            return None

    def set_option(self, section, option, value):
        if self.section_and_option_is(section, option):
            self.config.set(section, option, value)
            self.config.write(open(self.path, "w", encoding="utf-8"))

    def add_section(self, section):
        self.config.add_section(section)
        self.config.write(open(self.path, "w", encoding="utf-8"))

    def add_option(self, section, option):
        self.config.set(section, option, "")
        self.config.write(open(self.path, "w", encoding="utf-8"))

    def section_and_option_is(self, section, option):
        if self.config.has_section(section):
            if self.config.has_option(section, option):
                return True
            else:
                self.add_option(section, option)
                return False
        else:
            self.add_section(section)
            return False

    def create_config(self):
        folder = os.path.exists("./conf")
        if not folder:
            os.makedirs("./conf")
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                f.close()
