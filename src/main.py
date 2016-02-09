import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="pyqrtray")
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


def main():
    win = MainWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
