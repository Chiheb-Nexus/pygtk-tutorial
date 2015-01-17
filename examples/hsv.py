#!/usr/bin/env python

import gtk

class HSV:
    def __init__(self):
        window = gtk.Window()
        hsv = gtk.HSV()
        
        window.connect("destroy", lambda w: gtk.main_quit())
        hsv.connect("changed", self.colour_changed)
        
        window.add(hsv)
        window.show_all()
    
    def colour_changed(self, hsv):
        print hsv.get_color()

HSV()
gtk.main()
