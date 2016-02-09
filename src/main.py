import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
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

        self.image = Gtk.Image.new_from_pixbuf(pil_to_pixbuf(qrcode.make("test")))
        self.add(self.image)

        self.show_all()


def main():
    win = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
