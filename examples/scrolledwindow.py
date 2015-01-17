#!/usr/bin/env python

import gtk

class ScrolledWindow:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        scrolledwindow = gtk.ScrolledWindow()
        textview = gtk.TextView()
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(scrolledwindow)
        scrolledwindow.add(textview)
        window.show_all()

ScrolledWindow()
gtk.main()
