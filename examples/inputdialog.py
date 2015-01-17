#!/usr/bin/env python

import gtk

class InputDialog:
    def __init__(self):
        inputdialog = gtk.InputDialog()
        
        vbox = inputdialog.get_child()
        children = vbox.get_children()
        hbuttonbox = children[2]
        buttons = hbuttonbox.get_children()
        button_close = buttons[1]
        button_save = buttons[0]
        
        button_save.connect("clicked", self.interaction)
        button_close.connect("clicked", lambda w: inputdialog.destroy())

        inputdialog.run()
        inputdialog.destroy()
    
    def interaction(self, widget):
        print "Save Button clicked"

InputDialog()
