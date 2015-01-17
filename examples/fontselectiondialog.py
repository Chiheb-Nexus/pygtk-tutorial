#!/usr/bin/env python

import gtk

class FontSelectionDialog:
    def __init__(self):
        fontselectiondialog = gtk.FontSelectionDialog("FontSelectionDialog Example")
        
        response = fontselectiondialog.run()
        
        if response == gtk.RESPONSE_OK:
            print "Font selected:", fontselectiondialog.get_font_name()
        
        fontselectiondialog.destroy()

FontSelectionDialog()
