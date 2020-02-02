#!/usr/bin/env python3

import gi
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import GLib, Gdk, Gtk, WebKit2
from configparser import ConfigParser

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

# TODO: use
# parser = OptionParser()
# parser.add_option("-d", "--debug", help="Debug mode", metavar="DEBUG", default=False)
# (options, args) = parser.parse_args()

import sys
import json
from os import path

def die(err):
    log.error(err)
    sys.exit(2)

class Launcher(Gtk.Window):

    def __init__(self, app_dir, config):
        # Gtk.Window.__init__(self, title="Hello World")
        Gtk.Window.__init__(self)
        self.set_title("Hello")

        self.app_dir = app_dir
        self.config = config

        self.browser = WebKit2.WebView()

        settings = self.browser.get_settings()
        settings.set_property("allow-file-access-from-file-urls", True)

        if "title" in config:
            self.set_title(config['title'])

        self.main = path.abspath(path.join(app_dir, config['main']))
        if not path.exists(self.main):
            die("%s (main file) does not exist" % self.main)

        self.reset_browser()

        log.info("Displaying app")

        # self.button = Gtk.Button(label="Click Here")
        # self.button.connect("clicked", self.on_button_clicked)
        # self.add(self.button)
        self.add(self.browser)
        self.show_all()

    def reset_browser(self):
        log.info("Reseting browser to %s" % self.main)
        self.browser.load_uri("file://%s" % self.main)

    def on_button_clicked(self, widget):
        print("Hello World")

if __name__ == "__main__":
    folder = path.abspath(sys.argv[1])

    log.info("Loading app @ %s" % folder)

    config_file = path.join(folder, "package.json")

    if not path.exists(config_file):
        die("%s does not exist, not a launchable app" % config_file)

    with open(config_file) as f:
        config = json.load(f)

    if not "launcher" in config:
        die("%s does not contain required property config.launcher.main" % config_file)

    if not "main" in config['launcher']:
        die("%s does not contain required property config.launcher.main" % config_file)

    win = Launcher(app_dir=folder, config=config['launcher'])
    # win.connect("delete-event", Gtk.main_quit)
    win.show_all()

    # This launcher everything
    Gtk.main()
