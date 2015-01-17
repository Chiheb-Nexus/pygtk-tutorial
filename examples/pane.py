#!/usr/bin/env python

import gtk

class Pane:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(250, 100)
        
        label1 = gtk.Label("Label 1")
        label2 = gtk.Label("Label 2")
        
        pane = gtk.HPaned()
        pane.set_position(150)
        pane.add1(label1)
        pane.add2(label2)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(pane)
        window.show_all()
Pane()
gtk.main()
