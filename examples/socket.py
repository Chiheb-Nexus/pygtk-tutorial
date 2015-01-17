#!/usr/bin/env python

import gtk, sys, string

class Socket:
    def __init__(self):
        window = gtk.Window()     
        window.set_default_size(200, 200) 
        
        socket = gtk.Socket()
        window.add(socket)
        print "Socket ID:", socket.get_id()
        
        if len(sys.argv) == 2:
            socket.add_id(long(sys.argv[1]))
        
        window.connect("destroy", lambda w: gtk.main_quit())
        socket.connect("plug-added", self.plugged_event)
        
        window.show_all()
    
    def plugged_event(self, widget):
        print "A plug has been inserted."

Socket()
gtk.main()
