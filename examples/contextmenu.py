#!/usr/bin/env python

import gtk

class ContextMenu:
    def __init__(self):
        window = gtk.Window()
        eventbox = gtk.EventBox()
        
        self.menu = gtk.Menu()
        menuitem1 = gtk.MenuItem("MenuItem 1")
        menuitem2 = gtk.MenuItem("MenuItem 2")
        menuitem3 = gtk.MenuItem("MenuItem 3")
        self.menu.append(menuitem1)
        self.menu.append(menuitem2)
        self.menu.append(menuitem3)

        window.connect("destroy", lambda w: gtk.main_quit())
        eventbox.connect("button-release-event", self.menu_display)
        
        window.add(eventbox)
        window.show_all()
    
    def menu_display(self, widget, event):
        if event.button == 3:
            self.menu.popup(None, None, None, event.button, event.time, None)
            self.menu.show_all()

ContextMenu()
gtk.main()
