#!/usr/bin/env python

import gtk

class CellRendererText:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(str, str)
        liststore.append(["Fedora", "http://fedoraproject.org/"])
        liststore.append(["Slackware", "http://www.slackware.com/"])
        liststore.append(["Sidux", "http://sidux.com/"])
        
        treeview = gtk.TreeView(liststore)
        column_text = gtk.TreeViewColumn("Text")
        column_editabletext = gtk.TreeViewColumn("Editable Text")
        treeview.append_column(column_text)
        treeview.append_column(column_editabletext)
        
        cellrenderer_text = gtk.CellRendererText()
        column_text.pack_start(cellrenderer_text, False)
        column_text.add_attribute(cellrenderer_text, "text", 0)
        
        cellrenderer_editabletext = gtk.CellRendererText()
        cellrenderer_editabletext.set_property("editable", True)
        column_editabletext.pack_start(cellrenderer_editabletext, False)
        column_editabletext.add_attribute(cellrenderer_editabletext, "text", 1)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        cellrenderer_editabletext.connect("edited", self.text_edited, liststore)

        window.add(treeview)
        window.show_all()
    
    def text_edited(self, widget, path, text, model):
        model[path][1] = text

CellRendererText()
gtk.main()
