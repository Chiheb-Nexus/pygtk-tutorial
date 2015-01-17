#!/usr/bin/env python

import gtk

class Notebook:
    def __init__(self):
        window = gtk.Window()
        window.set_border_width(5)
        window.set_default_size(400, 250)
        
        hbox = gtk.HBox(False, 5)
        vbox = gtk.VBox(False, 5)
        
        self.notebook = gtk.Notebook()
        for i in range(1, 6):
            box = gtk.VBox()
            label = gtk.Label("Page " + str(i))
            self.notebook.append_page(box, label)
        
        self.check_border = gtk.CheckButton("Display Border")
        self.check_border.set_active(True)
        self.check_tabs = gtk.CheckButton("Display Tabs")
        self.check_tabs.set_active(True)
        self.check_scrollable = gtk.CheckButton("Allow Tab Scrolling")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.check_tabs.connect("toggled", self.display_tabs)
        self.check_border.connect("toggled", self.display_border)
        self.check_scrollable.connect("toggled", self.set_scrollable)
        
        window.add(hbox)
        hbox.pack_start(self.notebook, True, True, 0)
        hbox.pack_end(vbox, False, False, 0)
        vbox.pack_start(self.check_border, False, False, 0)
        vbox.pack_start(self.check_tabs, False, False, 0)
        vbox.pack_start(self.check_scrollable, False, False, 0)
        
        window.show_all()
    
    def display_border(self, widget):
        if self.check_border.get_active():
            self.notebook.set_show_border(True)
        else:
            self.notebook.set_show_border(False)        
    
    def display_tabs(self, widget):
        if self.check_tabs.get_active():
            self.notebook.set_show_tabs(True)
        else:
            self.notebook.set_show_tabs(False)

    def set_scrollable(self, widget):
        if self.check_scrollable.get_active():
            self.notebook.set_scrollable(True)
        else:
            self.notebook.set_scrollable(False)

Notebook()
gtk.main()
