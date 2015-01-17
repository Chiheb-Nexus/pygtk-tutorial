#!/usr/bin/env python

import gtk
import gobject

class CellRendererSpinner:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, bool, int)
        liststore.append(["Copying Files", True, 0])
        liststore.append(["Downloading Access Logs", False, 0])
        liststore.append(["Connecting To Torrent", True, 0])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_spinner = gtk.TreeViewColumn("Spinner")
        treeview.append_column(column_text)
        treeview.append_column(column_spinner)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_spinner = gtk.CellRendererSpinner()
        column_spinner.pack_start(cellrenderer_spinner, True)
        column_spinner.add_attribute(cellrenderer_spinner, "active", 1)

        window.connect("destroy", lambda w: gtk.main_quit())

        window.add(treeview)
        window.show_all()
        
        self.count = 0
        gobject.timeout_add(100, self.pulse, liststore, column_spinner, cellrenderer_spinner)
    
    def pulse(self, liststore, column, spinner):
        column.add_attribute(spinner, "pulse", 2)
        
        self.count+=1
        
        for item in liststore:
            item[2] = self.count
        
        return True

CellRendererSpinner()
gtk.main()
