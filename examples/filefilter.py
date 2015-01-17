#!/usr/bin/env python

import gtk

class FileFilter:
    def __init__(self):
        dialog = gtk.FileChooserDialog("Select a File", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK), None)
        
        filter_all = gtk.FileFilter()
        filter_all.set_name("All Files")
        filter_all.add_pattern("*")
        
        filter_images = gtk.FileFilter()
        filter_images.set_name("Images")
        filter_images.add_pattern("*.png")
        filter_images.add_pattern("*.jpg")
        filter_images.add_pattern("*.bmp")
        
        filter_sounds = gtk.FileFilter()
        filter_sounds.set_name("Sounds")
        filter_sounds.add_pattern("*.ogg")
        filter_sounds.add_pattern("*.flac")
        
        dialog.add_filter(filter_all)
        dialog.add_filter(filter_images)
        dialog.add_filter(filter_sounds)
        
        dialog.run()
        dialog.destroy()
        
FileFilter()
