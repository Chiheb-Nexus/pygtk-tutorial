#!/usr/bin/env python

import gtk

class Viewport:
    def __init__(self):
        window = gtk.Window()

        viewport = gtk.Viewport()
        viewport.set_size_request(200, 200)
        vadjustment = viewport.get_vadjustment()
        hadjustment = viewport.get_hadjustment()
        vscroll = gtk.VScrollbar(vadjustment)
        hscroll = gtk.HScrollbar(hadjustment)
        
        table = gtk.Table(2, 2, False)
        table.attach(viewport, 0, 1, 0, 1, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND)
        table.attach(vscroll, 1, 2, 0, 1, gtk.FILL | gtk.SHRINK, gtk.FILL | gtk.SHRINK)
        table.attach(hscroll, 0, 1, 1, 2, gtk.FILL | gtk.SHRINK, gtk.FILL | gtk.SHRINK)
        
        table2 = gtk.Table()
        for i in range(0, 15):
            button = gtk.Button(str(i))
            table2.attach(button, 0 + i, 1 + i, 0 + i, 1 + i)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(table)
        viewport.add(table2)
        window.show_all()

Viewport()
gtk.main()
