#!/usr/bin/env python

import gtk, sys

class Plug:
    def __init__(self):
        Wid = 0L
        if len(sys.argv) == 2:
            Wid = long(sys.argv[1])
        
        plug = gtk.Plug(Wid)
        print "Plug ID:", plug.get_id()
        
        entry = gtk.Entry()
        entry.set_text("PyGTK Plug & Socket")
        
        plug.connect("embedded", self.embed_event)
        plug.connect("destroy", lambda w: gtk.main_quit())
        entry.connect("activate", self.entry_changed)
        
        plug.add(entry)
        plug.show_all()
        
    def embed_event(self, widget):
        print "A plug has been embedded."
    
    def entry_changed(self, widget):
        print "Entry text has been changed to:", widget.get_text()

Plug()
gtk.main()
