#!/usr/bin/env python

import gtk

class CellView:
    def __init__(self):
        window = gtk.Window()

        vbox = gtk.VBox(False, 2)
        
        label = gtk.Label("Double click to activate cell")

        liststore = gtk.ListStore(str, str)
        liststore.append(["Debian", "http://www.debian.org/"])
        liststore.append(["Fedora", "http://fedoraproject.org/"])
        liststore.append(["Sabayon", "http://www.sabayon.org/"])
        liststore.append(["Chakra", "http://chakra-project.org/"])
        liststore.append(["Arch Linux", "http://www.archlinux.org/"])

        treeview = gtk.TreeView(liststore)
        
        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", cell)
        column.add_attribute(cell, "text", 0)
        treeview.append_column(column)
        
        cell = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Website", cell)
        column.add_attribute(cell, "text", 1)
        treeview.append_column(column)

        self.cellview = gtk.CellView()
        self.cellview.set_model(liststore)
        cell = gtk.CellRendererText()
        self.cellview.pack_start(cell, False)
        self.cellview.add_attribute(cell, "text", 0)
        cell = gtk.CellRendererText()
        self.cellview.pack_start(cell, False)
        self.cellview.add_attribute(cell, "text", 1)

        window.connect("destroy", lambda w: gtk.main_quit())
        treeview.connect("row-activated", self.row_selected)

        window.add(vbox)
        vbox.pack_start(label, False)
        vbox.pack_start(treeview, True)
        vbox.pack_start(self.cellview, False)
        window.show_all()
        
    def row_selected(self, treeview, path, column):
        self.cellview.set_displayed_row(path)

CellView()
gtk.main()
