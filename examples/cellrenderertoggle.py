#!/usr/bin/env python

import gtk

class CellRendererToggle:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, bool)
        liststore.append(["Debian", False])
        liststore.append(["OpenSuse", True])
        liststore.append(["Fedora", False])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_toggle = gtk.TreeViewColumn("Toggle")
        treeview.append_column(column_text)
        treeview.append_column(column_toggle)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_toggle = gtk.CellRendererToggle()
        column_toggle.pack_start(cellrenderer_toggle, True)
        column_toggle.add_attribute(cellrenderer_toggle, "active", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        cellrenderer_toggle.connect("toggled", self.cell_toggled, liststore)
        
        window.add(treeview)
        window.show_all()
    
    def cell_toggled(self, widget, path, model):
        model[path][1] = not model[path][1]

CellRendererToggle()
gtk.main()
