#!/usr/bin/env python

import gtk

class EntryBuffer:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 2)
        
        entrybuffer = gtk.EntryBuffer("Text set via EntryBuffer...", -1)
        
        entry = gtk.Entry()
        entry.set_buffer(entrybuffer)
        vbox.pack_start(entry, False)
        
        entry = gtk.Entry()
        entry.set_buffer(entrybuffer)
        vbox.pack_start(entry, False)
        
        entry = gtk.Entry()
        entry.set_buffer(entrybuffer)
        vbox.pack_start(entry, False)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(vbox)
        window.show_all()

EntryBuffer()
gtk.main()
