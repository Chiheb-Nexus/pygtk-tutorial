#!/usr/bin/env python

import gtk

class ColorSelection:
    def __init__(self):
        window = gtk.Window()
        colorselection = gtk.ColorSelection()
        
        window.connect("destroy", lambda w: gtk.main_quit())
        colorselection.connect("color-changed", self.color_selected)
        
        window.add(colorselection)
        
        window.show_all()
    
    def color_selected(self, widget):
        print "Colour selected:", widget.get_current_color()

ColorSelection()
gtk.main()
