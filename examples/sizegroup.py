#!/usr/bin/env python

import gtk

class SizeGroup:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        vbox = gtk.VBox(False, 2)
        
        sizegroup = gtk.SizeGroup(gtk.SIZE_GROUP_BOTH)
        
        for i in range(3):
            button = gtk.Button("Button %s" % int(i+1))
            sizegroup.add_widget(button)
            vbox.pack_start(button)
        
        button = gtk.Button("Button 4")
        sizegroup.add_widget(button)
        vbox.pack_start(button)
        
        window.connect("destroy", lambda w: gtk.main_quit())
               
        window.add(vbox)
        window.show_all()
        
SizeGroup()
gtk.main()
