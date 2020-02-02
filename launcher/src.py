import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

import sys
import json
from os import path

class Launcher(Gtk.Window):

    def __init__(self, app_dir, config):
        # Gtk.Window.__init__(self, title="Hello World")
        Gtk.Window.__init__(self)
        self.set_title("Hello")

        self.app_dir = app_dir
        self.config = config

        if "title" in config:
            self.set_title(config.title)

        main = path.abspath(path.join(app_dir, config.main))

        # self.button = Gtk.Button(label="Click Here")
        # self.button.connect("clicked", self.on_button_clicked)
        # self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

folder = path.abspath(sys.argv[1])

log.info("Loading app @ %s" % folder)

config_file = path.join(folder, "package.json")

with open(config_file) as f:
    config = json.load(f)

win = Launcher(app_dir=folder, config=config)
#  win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
