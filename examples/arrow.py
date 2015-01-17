#!/usr/bin/env python

import gtk

class Arrow:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(100, 25)
        hbox = gtk.HBox()
        
        arrow_up = gtk.Arrow(gtk.ARROW_UP, gtk.SHADOW_OUT)
        arrow_down = gtk.Arrow(gtk.ARROW_DOWN, gtk.SHADOW_OUT)
        arrow_left = gtk.Arrow(gtk.ARROW_LEFT, gtk.SHADOW_OUT)
        arrow_right = gtk.Arrow(gtk.ARROW_RIGHT, gtk.SHADOW_OUT)
        
        window.add(hbox)
        hbox.add(arrow_up)
        hbox.add(arrow_down)
        hbox.add(arrow_left)
        hbox.add(arrow_right)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.show_all()

Arrow()
gtk.main()
