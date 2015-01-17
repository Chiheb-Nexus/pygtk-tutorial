#!/usr/bin/env python

import gtk

class ColorSelectionDialog:
    def __init__(self):
        colorselectiondialog = gtk.ColorSelectionDialog("ColorSelectionDialog Example")
        selector = colorselectiondialog.get_color_selection()
        
        response = colorselectiondialog.run()

        if response == gtk.RESPONSE_OK:
            print "Colour selected:", selector.get_current_color()
        
        colorselectiondialog.destroy()

ColorSelectionDialog()
