#!/usr/bin/env python

import gtk

class FileChooserWidget:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(500, 350)
        window.set_border_width(5)
        
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox()
        
        self.filechooser = gtk.FileChooserWidget()
        self.filechooser.set_select_multiple(True)
        
        button = gtk.Button("OK")
        button.set_size_request(80, -1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("clicked", self.file_selected)
        
        window.add(vbox)
        vbox.pack_start(self.filechooser)
        vbox.pack_start(hbox, False, False, 0)
        hbox.pack_end(button, False, False, 0)
        
        window.show_all()
    
    def file_selected(self, widget):
        filenames = self.filechooser.get_filenames()
        for filename in filenames:
            print "Selected filepath: %s" % filename

FileChooserWidget()
gtk.main()
