#!/usr/bin/env python

import gtk

class ActionGroup:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        accelgroup = gtk.AccelGroup()
        window.add_accel_group(accelgroup)
        
        actiongroup = gtk.ActionGroup("actiongroup")
        actiongroup.add_actions([
                               ("new", gtk.STOCK_NEW, "New", None, "Create a dew document", self.button_clicked),
                               ("open", gtk.STOCK_OPEN, "Open", None, "Open an existing document", self.button_clicked),
                               ("save", gtk.STOCK_SAVE, "Save", None, "Save the current document", self.button_clicked)
                               ])
                               
        newaction = actiongroup.get_action("new")
        newtoolitem = newaction.create_tool_item()
        openaction = actiongroup.get_action("open")
        opentoolitem = openaction.create_tool_item()
        saveaction = actiongroup.get_action("save")
        savetoolitem = saveaction.create_tool_item()
        
        toolbar = gtk.Toolbar()
        toolbar.insert(newtoolitem, 0)
        toolbar.insert(opentoolitem, 1)
        toolbar.insert(savetoolitem, 2)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(toolbar)
        window.show_all()
    
    def button_clicked(self, widget):
        print "%s toolitem clicked" % widget.get_property("label")

ActionGroup()
gtk.main()
