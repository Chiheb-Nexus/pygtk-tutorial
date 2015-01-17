#!/usr/bin/env python

import gtk

class Curve:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 250)
        
        vbox = gtk.VBox(False, 5)
        
        self.curve = gtk.Curve()
        button_retrieve = gtk.Button("Retrieve")
        button_reset = gtk.Button("Reset")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button_retrieve.connect("clicked", self.points)
        button_reset.connect("clicked", lambda r: self.curve.reset())
        
        window.add(vbox)
        vbox.pack_start(self.curve, True, True, 0)
        vbox.pack_start(button_retrieve, False, False, 0)
        vbox.pack_start(button_reset, False, False, 0)
        
        window.show_all()
    
    def points(self, widget):
        print self.curve.get_vector(5)

Curve()
gtk.main()
