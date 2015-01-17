#!/usr/bin/env python

import gtk

class FontSelection:
    def __init__(self):
        window = gtk.Window()
        window.set_border_width(5)
        
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox()
        
        self.fontselection = gtk.FontSelection()
        button = gtk.Button("OK")
        button.set_size_request(80, -1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("clicked", self.interaction)
        
        window.add(vbox)
        vbox.pack_start(self.fontselection, True, True, 0)
        vbox.pack_start(hbox, False, False, 0)
        hbox.pack_end(button, False, False, 0)
        
        window.show_all()
    
    def interaction(self, widget):
        print "Font selected:", self.fontselection.get_font_name()

FontSelection()
gtk.main()
