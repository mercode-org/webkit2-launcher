#!/usr/bin/env python3

import gi
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import GLib, Gdk, Gtk, WebKit2
from optparse import OptionParser
# from configparser import ConfigParser

parser = OptionParser()
parser.add_option("-d", "--debug", help="Debug mode", metavar="DEBUG", default=False, action="store_true", dest="debug")
(options, args) = parser.parse_args()

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
if options.debug:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.INFO)

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

        self.main = self._resource_path(config['main'])

        self.reset_browser()

        # these are processed in the same order as docs. if not, add a comment.

        if "title" in config:
            self.set_title(config['title'])

        if "width" in config or "height" in config: # both require each other
            self.set_default_size(config['width'], config['height'])

        # minWidth & minHeight todo

        if "iconPath" in config:
            self.set_icon_from_file(self._resource_path(config['iconPath']))

        if "icon" in config:
            self.set_icon_name(config['icon'])

        log.debug("Displaying app")

        # self.button = Gtk.Button(label="Click Here")
        # self.button.connect("clicked", self.on_button_clicked)
        # self.add(self.button)
        self.add(self.browser)
        self.show_all()

    def _resource_path(self, resource, check_exists=True):
        res_path = path.abspath(path.join(self.app_dir, resource))
        log.debug("resource path %s" % res_path)
        if check_exists and not path.exists(res_path):
            die("%s does not exist, but is required" % res_path)

        return res_path

    def reset_browser(self):
        log.debug("Reseting browser to %s" % self.main)
        self.browser.load_uri("file://%s" % self.main)

    def on_button_clicked(self, widget):
        print("Hello World")

if __name__ == "__main__":
    if len(args):
        folder = path.abspath(args[0])
    else:
        folder = path.abspath(path.join(path.dirname(__file__), '..', 'example'))

    log.debug("Loading app @ %s" % folder)

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
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    # This launcher everything
    Gtk.main()
