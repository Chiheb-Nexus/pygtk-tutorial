#!/usr/bin/env python

import gtk

class CellRendererPixbuf:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, str)
        liststore.append(["New", gtk.STOCK_NEW])
        liststore.append(["Open", gtk.STOCK_OPEN])
        liststore.append(["Save", gtk.STOCK_SAVE])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_pixbuf = gtk.TreeViewColumn("Image")
        treeview.append_column(column_text)
        treeview.append_column(column_pixbuf)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_pixbuf = gtk.CellRendererPixbuf()
        column_pixbuf.pack_start(cellrenderer_pixbuf, False)
        column_pixbuf.add_attribute(cellrenderer_pixbuf, "stock-id", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())

        window.add(treeview)
        window.show_all()

CellRendererPixbuf()
gtk.main()
