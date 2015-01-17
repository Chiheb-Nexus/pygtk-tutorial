#!/usr/bin/env python

import gtk

class Entry:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)
        
        self.entry = gtk.Entry()
        self.entry.set_text("PyGTK Tutorial")
        self.check_editable = gtk.CheckButton("Entry text editable")
        self.check_editable.set_active(True)
        self.check_visible = gtk.CheckButton("Entry text visible")
        self.check_visible.set_active(True)
        
        vbox.pack_start(self.entry, False, False, 0)
        vbox.pack_start(self.check_editable, False, False, 0)
        vbox.pack_start(self.check_visible, False, False, 0)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.check_editable.connect("toggled", self.editable)
        self.check_visible.connect("toggled", self.visible)
        
        window.add(vbox)
        window.show_all()
    
    def editable(self, widget):
        if self.check_editable.get_active() == False:
            self.entry.set_editable(False)
        else:
            self.entry.set_editable(True)
    
    def visible(self, widget):
        if self.check_visible.get_active() == False:
            self.entry.set_visibility(False)
        else:
            self.entry.set_visibility(True)

Entry()
gtk.main()
