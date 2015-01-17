#!/usr/bin/env python

import gtk

class RecentChooserWidget:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)

        self.manager = gtk.RecentManager()
        self.recentchooser = gtk.RecentChooserWidget(self.manager)
        button = gtk.Button("Recent Information")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("clicked", self.retrieve_info)
        
        window.add(vbox)
        vbox.pack_start(self.recentchooser)
        vbox.pack_start(button, False, False, 0)
        window.show_all()
    
    def retrieve_info(self, widget):
        selected = self.recentchooser.get_current_item()
        print "Display name:", selected.get_display_name()
        print "File URI:", selected.get_uri()
        print "Last application:", selected.last_application()

RecentChooserWidget()
gtk.main()
