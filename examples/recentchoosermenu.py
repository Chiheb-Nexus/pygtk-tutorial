#!/usr/bin/env python

import gtk

class RecentChooserMenu:
    def __init__(self):
        window = gtk.Window()
        
        manager = gtk.recent_manager_get_default()
        self.recentchooser = gtk.RecentChooserMenu(manager)
        
        menubar = gtk.MenuBar()
        file_menuitem = gtk.MenuItem("Recent Items")
        menubar.append(file_menuitem)
        
        file_menuitem.set_submenu(self.recentchooser)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.recentchooser.connect("item-activated", self.display_info)
        
        window.add(menubar)
        
        window.show_all()
    
    def display_info(self, widget):
        selected = self.recentchooser.get_current_item()
        print "Display name:", selected.get_display_name()
        print "File URI:", selected.get_uri()
        print "Last application:", selected.last_application()

RecentChooserMenu()
gtk.main()
