#!/usr/bin/env python

import gtk

class Toolbar:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(500, -1)
        
        toolbar = gtk.Toolbar()
        
        button1 = gtk.ToolButton(gtk.STOCK_ADD)
        button2 = gtk.ToolButton(gtk.STOCK_REMOVE)
        separator1 = gtk.SeparatorToolItem()
        toggle = gtk.ToggleToolButton(gtk.STOCK_MEDIA_PLAY)
        separator2 = gtk.SeparatorToolItem()
        menu1 = gtk.MenuToolButton(gtk.STOCK_GO_BACK)
        menu2 = gtk.MenuToolButton(gtk.STOCK_GO_FORWARD)
        separator3 = gtk.SeparatorToolItem()
        radio1 = gtk.RadioToolButton(None, gtk.STOCK_NEW)
        radio2 = gtk.RadioToolButton(radio1, gtk.STOCK_OPEN)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(toolbar)
        toolbar.insert(button1, 0)
        toolbar.insert(button2, 1)
        toolbar.insert(separator1, 2)
        toolbar.insert(toggle, 3)
        toolbar.insert(separator2, 4)
        toolbar.insert(menu1, 5)
        toolbar.insert(menu2, 6)
        toolbar.insert(separator3, 7)
        toolbar.insert(radio1, 8)
        toolbar.insert(radio2, 9)
        
        window.show_all()

Toolbar()
gtk.main()
