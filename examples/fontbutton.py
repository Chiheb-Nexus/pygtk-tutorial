#!/usr/bin/env python

import gtk

class FontButton:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        fontbutton = gtk.FontButton()

        window.connect("destroy", gtk.main_quit)
        fontbutton.connect("font-set", self.font_selected)
        
        window.add(fontbutton)
        window.show_all()
    
    def font_selected(self, widget):
        print "Font selected:", widget.get_font_name()
        
FontButton()
gtk.main()
