import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from gi.repository import GLib
import qrcode


def image2pixbuf(im):
    """
    Adapted from http://stackoverflow.com/questions/7906814/converting-pil-image-to-gtk-pixbuf and
    https://gist.github.com/mozbugbox/10cd35b2872628246140
    """
    arr = GLib.Bytes.new(im.convert("RGB").tobytes())
    width, height = im.size
    return GdkPixbuf.Pixbuf.new_from_bytes(arr, GdkPixbuf.Colorspace.RGB, False, 8, width, height, width * 3)


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="pyqrtray")
        self.connect("delete-event", Gtk.main_quit)

        img = qrcode.make("test")
        self.pix = image2pixbuf(img)

        self.img = Gtk.Image.new_from_pixbuf(self.pix)
        self.add(self.img)

        self.show_all()


def main():
    win = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
