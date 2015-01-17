#!/usr/bin/env python

import gtk

class CellRendererAccel:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, str)
        liststore.append(["Up", "Up"])
        liststore.append(["Down", "Down"])
        liststore.append(["Left", "Left"])
        liststore.append(["Right", "Right"])
        liststore.append(["Fire", "Return"])
        liststore.append(["Menu", "Escape"])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_accel = gtk.TreeViewColumn("Accelerator")
        treeview.append_column(column_text)
        treeview.append_column(column_accel)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_accel = gtk.CellRendererAccel()
        cellrenderer_accel.set_property("editable", True)
        column_accel.pack_start(cellrenderer_accel, True)
        column_accel.add_attribute(cellrenderer_accel, "text", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        cellrenderer_accel.connect("accel-edited", self.accel_edited, liststore)
        cellrenderer_accel.connect("accel-cleared", self.accel_cleared, liststore)

        window.add(treeview)
        window.show_all()

    def accel_edited(self, widget, path, key, mods, hwcode, model):
        accel = gtk.accelerator_name(key, mods)
        iter = model.get_iter(path)
        model.set_value(iter, 1, accel)

    def accel_cleared(self, widget, path, model):
        iter = model.get_iter(path)
        model.set_value(iter, 1, None)

CellRendererAccel()
gtk.main()
