#!/usr/bin/env python

import gtk

class TooltipBasic:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        vbox = gtk.VBox(True, 5)
        button = gtk.Button("Button")
        button.set_tooltip_text("Button Tooltip")
        label = gtk.Label("Label")
        label.set_tooltip_text("Label Tooltip")
        entry = gtk.Entry()
        entry.set_tooltip_text("Entry Tooltip")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(vbox)
        vbox.add(button)
        vbox.add(label)
        vbox.add(entry)
        window.show_all()

TooltipBasic()
gtk.main()
