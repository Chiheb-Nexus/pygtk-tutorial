#!/usr/bin/env python

import gtk

class ToolPalette:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(250, 500)
        
        toolpalette = gtk.ToolPalette()
        toolbutton1 = gtk.ToolButton(gtk.STOCK_ADD)
        toolbutton2 = gtk.ToolButton(gtk.STOCK_REMOVE)
        toolbutton3 = gtk.ToolButton(gtk.STOCK_ABOUT)
        toolbutton4 = gtk.ToolButton(gtk.STOCK_HELP)
        toolbutton5 = gtk.ToolButton(gtk.STOCK_PREFERENCES)
        
        group1 = gtk.ToolItemGroup("Group 1")
        group1.add(toolbutton1)
        group1.add(toolbutton2)
        toolpalette.add(group1)
        group2 = gtk.ToolItemGroup("Group 2")
        group2.add(toolbutton3)
        group2.add(toolbutton4)
        group2.add(toolbutton5)
        toolpalette.add(group2)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(toolpalette)
        window.show_all()
        toolpalette.show()

ToolPalette()
gtk.main()
