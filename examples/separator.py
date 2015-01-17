#!/usr/bin/env python

import gtk

class Separator:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(400, 200)
        
        hbox = gtk.HBox(False, 5)
        
        hseparator = gtk.HSeparator()
        vseparator = gtk.VSeparator()
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(hbox)
        hbox.pack_start(hseparator)
        hbox.pack_start(vseparator)
        
        window.show_all()

Separator()
gtk.main()
