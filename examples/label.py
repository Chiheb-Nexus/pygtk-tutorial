#!/usr/bin/env python

import gtk

class Label:
    def __init__(self):
        window = gtk.Window()
        
        hbox = gtk.HBox(False, 10)
        vbox_left = gtk.VBox(False, 10)
        vbox_right = gtk.VBox(False, 10)
        
        hbox.pack_start(vbox_left)
        hbox.pack_start(vbox_right)
        
        label = gtk.Label("This is a normal label")
        vbox_left.pack_start(label)
        
        label = gtk.Label("This is a left-justified label.\nWith multiple lines.")
        label.set_justify(gtk.JUSTIFY_LEFT)
        vbox_left.pack_start(label) 
        
        label = gtk.Label("This is a right-justified label.\nWith multiple lines.")
        label.set_justify(gtk.JUSTIFY_RIGHT)
        vbox_left.pack_start(label)
        
        label = gtk.Label("This is a line-wrapped label spread over multiple lines."
                          "It supports multiple lines and correctly inserts many   spaces   .")
        label.set_line_wrap(True)
        vbox_right.pack_start(label)
        
        label = gtk.Label("This is a line-wrapped, filled label. It takes the entire space "
                          "allocated to it.\n\nIt also supports multiple lines and correctly "
                          "inserts many   spaces   .")
        label.set_line_wrap(True)
        label.set_justify(gtk.JUSTIFY_FILL)
        vbox_right.pack_start(label)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(hbox)
        window.show_all()
        
Label()
gtk.main()
