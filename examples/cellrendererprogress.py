#!/usr/bin/env python

import gtk

class CellRendererProgress:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, int)
        liststore.append(["Sabayon", 75])
        liststore.append(["Zenwalk", 20])
        liststore.append(["SimplyMepis", 62])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_progress = gtk.TreeViewColumn("Progress Bar")
        treeview.append_column(column_text)
        treeview.append_column(column_progress)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_progress = gtk.CellRendererProgress()
        column_progress.pack_start(cellrenderer_progress, True)
        column_progress.add_attribute(cellrenderer_progress, "value", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())

        window.add(treeview)
        window.show_all()

CellRendererProgress()
gtk.main()
