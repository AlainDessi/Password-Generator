#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PswdGenerator import PswdGenerator

# Windows
class PasswordGenerator:
    __gtype_name__ = "Password Generator"

    def __init__(self):
        self.nbCharPassword = 8

        interface = Gtk.Builder()

        interface.add_from_file("window.glade")
        interface.connect_signals(self)

        window              = interface.get_object("window1")
        self.passwordOutput = interface.get_object("passwordOutput")
        self.comboNbChar    = interface.get_object("comboNbChar")

        window.show_all()

    def on_btnExit_clicked(self, widget):
        exit()

    def on_btnGenerate_clicked(self, widget):
        pswd = PswdGenerator(self.nbCharPassword)
        # génération du mot de Passe
        password = pswd.generatePswd()
        # Affichage du password
        self.passwordOutput.set_text(password)

    def on_comboNbChar_changed(self, widget):
        self.nbCharPassword = int(widget.get_active_text())

    def on_menuExit_activate(self, widget):
        exit()

# Main program
if __name__ == '__main__' :
    PasswordGenerator()
    Gtk.main()
    exit()
