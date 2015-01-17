#!/usr/bin/env python

import gtk

class Box:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 100)
        vbox = gtk.VBox(False, 5)
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        
        window.add(vbox)
        vbox.pack_start(button1)
        vbox.pack_start(button2)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.show_all()

Box()
gtk.main()
