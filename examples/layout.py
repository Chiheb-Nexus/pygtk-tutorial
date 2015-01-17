#!/usr/bin/env python

import gtk

class Layout:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        layout = gtk.Layout()
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        
        layout.put(button1, 50, 5)
        layout.put(button2, 110, 80)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(layout)
        window.show_all()

Layout()
gtk.main()
