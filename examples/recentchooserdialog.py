#!/usr/bin/env python

import gtk

class RecentChooserDialog:
    def __init__(self):
        manager = gtk.RecentManager()
        recentchooser = gtk.RecentChooserDialog("Select a file", None, manager, (gtk.STOCK_OK, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
        
        response = recentchooser.run()
        
        if response == gtk.RESPONSE_OK:
            selected = recentchooser.get_current_item()
            print "Display name:", selected.get_display_name()
            print "File URI:", selected.get_uri()
            print "Last application:", selected.last_application()
        
        recentchooser.destroy()

RecentChooserDialog()
