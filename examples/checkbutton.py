#!/usr/bin/env python

import gtk

class CheckButton:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox()
        checkbutton1 = gtk.CheckButton("CheckButton 1")
        checkbutton2 = gtk.CheckButton("CheckButton 2")

        vbox.pack_start(checkbutton1, False, False, 0)
        vbox.pack_start(checkbutton2, False, False, 0)
            
        window.connect("destroy", lambda w: gtk.main_quit())
            
        window.add(vbox)
        window.show_all()

CheckButton()
gtk.main()
