#!/usr/bin/env python

import gtk

class ScaleButton:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(100, 100)
        scalebutton = gtk.ScaleButton(gtk.ICON_SIZE_MENU, 0, 100, 2, (gtk.STOCK_ZOOM_FIT, gtk.STOCK_ZOOM_FIT))
        
        window.connect("destroy", lambda w: gtk.main_quit())
        scalebutton.connect("value-changed", self.value_changed)
        
        window.add(scalebutton)
        window.show_all()
    
    def value_changed(self, scalebutton, value):
        print "Scale Button is set to %i" % value

ScaleButton()
gtk.main()
