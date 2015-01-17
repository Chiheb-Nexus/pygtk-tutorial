#!/usr/bin/env python

import gtk

class TooltipAdvanced:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        vbox = gtk.VBox(True, 5)
        button = gtk.Button("Button")
        button.set_has_tooltip(True)
        label = gtk.Label("Label")
        label.set_has_tooltip(True)
        entry = gtk.Entry()
        entry.set_has_tooltip(True)

        window.connect("destroy", lambda w: gtk.main_quit())
        button.connect("query-tooltip", self.tooltip, "Button")
        label.connect("query-tooltip", self.tooltip, "Label")
        entry.connect("query-tooltip", self.tooltip, "Entry")
        
        window.add(vbox)
        vbox.pack_start(button)
        vbox.pack_start(label)
        vbox.pack_start(entry)
        window.show_all()
    
    def tooltip(self, item, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text("%s Tooltip" % text)
        tooltip.set_icon_from_stock(gtk.STOCK_HOME, gtk.ICON_SIZE_MENU)
        return True

TooltipAdvanced()
gtk.main()
