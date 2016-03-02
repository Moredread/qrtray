import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import GObject

import qrcode


def pil_to_pixbuf(image):
    """
    Adapted from http://stackoverflow.com/questions/7906814/converting-pil-image-to-gtk-pixbuf and
    https://gist.github.com/mozbugbox/10cd35b2872628246140
    """
    arr = GLib.Bytes.new(image.convert("RGB").tobytes())
    width, height = image.size
    return GdkPixbuf.Pixbuf.new_from_bytes(arr, GdkPixbuf.Colorspace.RGB, False, 8, width, height, width * 3)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="pyqrtray")

        color = Gdk.color_parse('white')
        self.modify_bg(Gtk.StateType.NORMAL, color)

        self.image = Gtk.Image()
        self.add(self.image)
        self.old_clipboard_content = None

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.check_clipboard()
        self.clipboard_callback_id = GLib.timeout_add(1000, self.__check_clipboard_callback)

        self.connect("delete-event", self.__window_close_handler)

        self.show_all()

    def update_qrcode(self, text):
        self.__update_image_from_qrcode(text, self.image)

    def __update_image_from_qrcode(self, text, image):
        qr = self.__make_qrcode(text)
        if qr != None:
            image.set_from_pixbuf(pil_to_pixbuf(self.__make_qrcode(text)))

    def __make_qrcode(self, text):
        try:
            return qrcode.make(text, border=0, error_correction=qrcode.constants.ERROR_CORRECT_L)
        except qrcode.exceptions.DataOverflowError:
            return None

    def __window_close_handler(self, window, event):
        print("Closing window")
        self.stop_clipboard_listener()

    def stop_clipboard_listener(self):
        if self.clipboard_callback_id is not None:
            GLib.source_remove(self.clipboard_callback_id)
            self.clipboard_callback_id = None

    def check_clipboard(self):
        text = self.clipboard.wait_for_text()
        if text is not None and text != self.old_clipboard_content:
            self.update_qrcode(text)
            self.old_clipboard_content = text

    def __check_clipboard_callback(self):
        self.check_clipboard()
        return True

    def __del__(self):
        print("window removed")
        self.stop_clipboard_listener()


class MainStatusIcon(Gtk.StatusIcon):
    def __init__(self):
        self.window = None
        self.menu = None

        Gtk.StatusIcon.__init__(self)
        self.set_from_stock(Gtk.STOCK_ABOUT)

        self.connect("activate", self.__activate_handler)
        self.connect("popup-menu", self.__popup_menu_handler)

    def create_menu(self, button, activate_time):
        menu = Gtk.Menu()

        toggle_window_item = Gtk.MenuItem("Toggle")
        exit_item = Gtk.MenuItem("Exit")

        toggle_window_item.connect("activate", self.__activate_handler)
        exit_item.connect("activate", Gtk.main_quit)

        menu.append(toggle_window_item)
        menu.append(exit_item)
        menu.show_all()

        menu.popup(None, None, None, None, button, activate_time)

        return menu

    def __popup_menu_handler(self, icon, button, activate_time):
        self.menu = self.create_menu(button, activate_time)

    def __activate_handler(self, event):
        self.toggle_window()

    def __window_close_handler(self, window, event):
        self.window = None

    def toggle_window(self):
        if self.window is None:
            self.window = MainWindow()
            self.window.connect("delete-event", self.__window_close_handler)
        else:
            self.window.close()
            self.window = None


def main():
    GObject.threads_init()

    icon = MainStatusIcon()

    Gtk.main()


if __name__ == "__main__":
    main()
