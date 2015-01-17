#!/usr/bin/env python

import gtk

class Scale:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        adjustment = gtk.Adjustment(0, 0, 100, 5, 10, 0)
        self.scale = gtk.HScale(adjustment)
        self.scale.set_digits(0)
        self.scale.set_update_policy(gtk.UPDATE_DELAYED)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.scale.connect("value-changed", self.scale_moved)
        
        window.add(self.scale)
        window.show_all()
        
    def scale_moved(self, widget):
        print self.scale.get_value()
        
Scale()
gtk.main()
