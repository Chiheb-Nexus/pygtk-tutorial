#!/usr/bin/env python

import gtk

class CellRendererSpin:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, int)
        liststore.append(["Oranges", 5])
        liststore.append(["Apples", 4])
        liststore.append(["Bananas", 2])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_spin = gtk.TreeViewColumn("Spin Button")
        treeview.append_column(column_text)
        treeview.append_column(column_spin)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        adjustment = gtk.Adjustment(0, 0, 100, 1, 10, 0)        
        cellrenderer_spin = gtk.CellRendererSpin()
        cellrenderer_spin.set_property("editable", True)
        cellrenderer_spin.set_property("adjustment", adjustment)
        column_spin.pack_start(cellrenderer_spin, True)
        column_spin.add_attribute(cellrenderer_spin, "text", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        cellrenderer_spin.connect("edited", self.spin_changed, liststore)
        
        window.add(treeview)
        window.show_all()
    
    def spin_changed(self, widget, path, value, model):
        model[path][1] = int(value)        

CellRendererSpin()
gtk.main()
