#!/usr/bin/env python

import gtk

class FileChooserButton:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        filechooserbutton = gtk.FileChooserButton("Select A File", None)

        window.connect("destroy", lambda w: gtk.main_quit())
        filechooserbutton.connect("file-set", self.file_selected)        
        
        window.add(filechooserbutton)
        window.show_all()
    
    def file_selected(self, widget):
        print "Selected filepath: %s" % widget.get_filename()

FileChooserButton()
gtk.main()
