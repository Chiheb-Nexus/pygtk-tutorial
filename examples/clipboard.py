#!/usr/bin/env python

import gtk

class Clipboard:
    def __init__(self):
        window = gtk.Window()
        hbox = gtk.HBox(False, 5)
        hbox2 = gtk.HBox(True, 5)
        
        self.entry = gtk.Entry()
        button_cut = gtk.Button("Cut Text")
        button_copy = gtk.Button("Copy Text")
        button_paste = gtk.Button("Paste Text")
        
        hbox.pack_start(self.entry)
        hbox.pack_start(hbox2)
        hbox2.pack_start(button_cut)
        hbox2.pack_start(button_copy)
        hbox2.pack_start(button_paste)
        window.add(hbox)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button_cut.connect("clicked", self.copy, "cut")
        button_copy.connect("clicked", self.copy, "copy")
        button_paste.connect("clicked", self.paste)
        
        window.show_all()
        
        self.clipboard = gtk.Clipboard(gtk.gdk.display_get_default(), "CLIPBOARD")
    
    def copy(self, widget, mode):
        self.clipboard.set_text(self.entry.get_text())
        
        if mode == "cut":
            self.entry.set_text("")
    
    def paste(self, widget):
        text = self.clipboard.wait_for_text()
        if text != None:
            self.entry.set_text(text)
        
Clipboard()
gtk.main()
