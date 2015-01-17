#!/usr/bin/env python

import gtk

class CellRendererCombo:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore_manufacturers = gtk.ListStore(str)
        manufacturers = ["Sony", "LG", "Panasonic", "Toshiba", "Nokia", "Samsung"]
        for item in manufacturers:
            liststore_manufacturers.append([item])
        
        liststore_hardware = gtk.ListStore(str, str)
        liststore_hardware.append(["Television", "Samsung"])
        liststore_hardware.append(["Mobile Phone", "LG"])
        liststore_hardware.append(["DVD Player", "Sony"])
        
        treeview = gtk.TreeView(liststore_hardware)
        column_text = gtk.TreeViewColumn("Text")
        column_combo = gtk.TreeViewColumn("Combo")
        treeview.append_column(column_text)
        treeview.append_column(column_combo)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_combo = gtk.CellRendererCombo()
        cellrenderer_combo.set_property("editable", True)
        cellrenderer_combo.set_property("model", liststore_manufacturers)
        cellrenderer_combo.set_property("text-column", 0)
        column_combo.pack_start(cellrenderer_combo, False)
        column_combo.add_attribute(cellrenderer_combo, "text", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        cellrenderer_combo.connect("edited", self.combo_changed, liststore_hardware)

        window.add(treeview)
        window.show_all()
    
    def combo_changed(self, widget, path, text, model):
        model[path][1] = text
        
CellRendererCombo()
gtk.main()
