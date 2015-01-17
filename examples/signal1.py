#!/usr/bin/env python

import gtk

class Signal:
    def __init__(self):
        window = gtk.Window()
        button = gtk.Button("Run an event")
        
        window.add(button)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("clicked", self.run_function, "Run an event")
        
        window.show_all()
    
    def run_function(self, widget, data):
        print data, "button was clicked"

Signal()
gtk.main()
