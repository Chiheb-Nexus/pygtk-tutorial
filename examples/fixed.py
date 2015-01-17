#!/usr/bin/env python

import gtk

class Fixed:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        fixed = gtk.Fixed()
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        
        fixed.put(button1, 50, 5)
        fixed.put(button2, 110, 80)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(fixed)
        window.show_all()

Fixed()
gtk.main()
