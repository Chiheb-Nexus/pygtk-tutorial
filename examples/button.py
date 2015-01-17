#!/usr/bin/env python

import gtk

class Button:
    def __init__(self):
        window = gtk.Window()
        button = gtk.Button("Button")
 
        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("clicked", self.button_clicked)
        
        window.add(button)
        window.show_all()
    
    def button_clicked(self, widget):
        print "Button was pressed"

Button()
gtk.main()
