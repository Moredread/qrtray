import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import GLib
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
        self.connect("delete-event", Gtk.main_quit)

        self.image = Gtk.Image()
        self.add(self.image)

        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        text = clipboard.wait_for_text()
        if text is not None:
            self.update_qrcode(text)

        self.show_all()

    def update_qrcode(self, text):
        self._update_image_from_qrcode(text, self.image)

    def _update_image_from_qrcode(self, text, image):
        image.set_from_pixbuf(pil_to_pixbuf(qrcode.make(text, border = 0, error_correction=qrcode.constants.ERROR_CORRECT_L)))

def main():
    win = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
