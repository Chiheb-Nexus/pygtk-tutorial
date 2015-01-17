#!/usr/bin/env python

import gtk

class Dialog:       
    def __init__(self):
        dialog = gtk.Dialog("Dialog Example", None, 0, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
        dialog.set_default_size(250, 300)
        label = gtk.Label("PyGTK Dialog")
        
        dialog.vbox.pack_start(label, True, True, 0)
        dialog.show_all()
        
        response = dialog.run()
        
        if response == gtk.RESPONSE_OK:
            print "The OK button was clicked"
        elif response == gtk.RESPONSE_CANCEL:
            print "The Cancel button was clicked"
        
        dialog.destroy()

Dialog()
