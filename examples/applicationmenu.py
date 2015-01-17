#!/usr/bin/env python

import gtk

class ApplicationMenu:
    def __init__(self):
        window = gtk.Window()

        menubar = gtk.MenuBar()
        
        menu_file = gtk.Menu()
        menu_edit = gtk.Menu()
        menu_help = gtk.Menu()
        
        item_open = gtk.MenuItem("Open")
        item_save = gtk.MenuItem("Save")
        item_quit = gtk.MenuItem("Quit")
        menu_file.append(item_open)
        menu_file.append(item_save)
        menu_file.append(item_quit)

        item_cut = gtk.MenuItem("Cut")
        item_copy = gtk.MenuItem("Copy")
        item_paste = gtk.MenuItem("Paste")
        menu_edit.append(item_cut)
        menu_edit.append(item_copy)
        menu_edit.append(item_paste)
        
        item_about = gtk.MenuItem("About")
        menu_help.append(item_about)
        
        item_file = gtk.MenuItem("File")
        item_edit = gtk.MenuItem("Edit")
        item_help = gtk.MenuItem("Help")
        
        item_file.set_submenu(menu_file)
        item_edit.set_submenu(menu_edit)
        item_help.set_submenu(menu_help)
        
        menubar.append(item_file)
        menubar.append(item_edit)
        menubar.append(item_help)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(menubar)
        window.show_all()

ApplicationMenu()
gtk.main()
