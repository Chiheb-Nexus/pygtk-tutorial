#!/usr/bin/env python

import gtk

class RadioAction:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(300, -1)
        vbox = gtk.VBox()
        
        menubar = gtk.MenuBar()
        menu_file = gtk.Menu()
        
        action_file = gtk.Action("File", "_File", None, None)
        action_new = gtk.RadioAction("New", "_New", "New Document", gtk.STOCK_NEW, 0)
        action_open = gtk.RadioAction("Open", "_Open", "Open Document", gtk.STOCK_OPEN, 1)
        action_save = gtk.RadioAction("Save", "_Save", "Save Document", gtk.STOCK_SAVE, 2)
        action_new.set_active(True)
        action_open.set_group(action_new)
        action_save.set_group(action_new)
        
        actiongroup = gtk.ActionGroup("actions")
        actiongroup.add_action(action_file)
        actiongroup.add_action(action_new)
        actiongroup.add_action(action_open)
        actiongroup.add_action(action_save)

        menuitem_file = action_file.create_menu_item()
        menubar.append(menuitem_file)
        menuitem_file.set_submenu(menu_file)
        
        menuitem_new = action_new.create_menu_item()
        menu_file.add(menuitem_new)
        menuitem_open = action_open.create_menu_item()
        menu_file.add(menuitem_open)
        menuitem_save = action_save.create_menu_item()
        menu_file.add(menuitem_save)
        
        toolbar = gtk.Toolbar()
        toolitem_new = action_new.create_tool_item()
        toolbar.add(toolitem_new)
        toolitem_open = action_open.create_tool_item()
        toolbar.add(toolitem_open)
        toolitem_save = action_save.create_tool_item()
        toolbar.add(toolitem_save)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        action_new.connect("activate", self.item_activated)
        action_open.connect("activate", self.item_activated)
        action_save.connect("activate", self.item_activated)
        
        window.add(vbox)
        vbox.pack_start(menubar, False)
        vbox.pack_start(toolbar, False)
        window.show_all()
    
    def item_activated(self, widget):
        print "Item activated"

RadioAction()
gtk.main()
