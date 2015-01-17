#!/usr/bin/env python

import gtk

class EventBox:
    def __init__(self):
        window = gtk.Window()
        label = gtk.Label("Label in an EventBox")
        eventbox = gtk.EventBox()
        
        window.connect("destroy", lambda w: gtk.main_quit())
        eventbox.connect("button_press_event", self.eventbox_event)
        
        window.add(eventbox)
        eventbox.add(label)
        window.show_all()
    
    def eventbox_event(self, widget, event):
        print "Label received a click!"

EventBox()
gtk.main()
