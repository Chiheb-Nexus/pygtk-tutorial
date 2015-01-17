#!/usr/bin/env python

import gtk

class Scrollbar:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        
        layout = gtk.Layout()
        layout.set_size(800, 400)
        layout.put(button1, 20, 20)
        layout.put(button2, 700, 350)
        
        vadjust = layout.get_vadjustment()
        hadjust = layout.get_hadjustment()        
        
        vscroll = gtk.VScrollbar(vadjust)
        hscroll = gtk.HScrollbar(hadjust)
        
        table = gtk.Table(2, 2, False)
        table.attach(layout, 0, 1, 0, 1, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND)
        table.attach(vscroll, 1, 2, 0, 1, gtk.FILL | gtk.SHRINK, gtk.FILL | gtk.SHRINK)
        table.attach(hscroll, 0, 1, 1, 2, gtk.FILL | gtk.SHRINK, gtk.FILL | gtk.SHRINK)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(table)
        window.show_all()

Scrollbar()
gtk.main()
