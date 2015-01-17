#!/usr/bin/env python

import gtk

class FileChooserDialog:
    def __init__(self):
        filechooserdialog = gtk.FileChooserDialog("FileChooserDialog Example", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
        
        response = filechooserdialog.run()
        
        if response == gtk.RESPONSE_OK:
            print "Selected filepath: %s" % filechooserdialog.get_filename()
        
        filechooserdialog.destroy()

FileChooserDialog()
