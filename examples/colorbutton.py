#!/usr/bin/env python

import gtk

class ColorButton:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        colorbutton = gtk.ColorButton(gtk.gdk.Color(0, 0, 0))

        window.connect("destroy", lambda w: gtk.main_quit())
        colorbutton.connect("color-set", self.color_selected)
        
        window.add(colorbutton)
        window.show_all()
    
    def color_selected(self, widget):
        print "Colour selected:", widget.get_color()
        
ColorButton()
gtk.main()
