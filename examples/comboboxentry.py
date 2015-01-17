#!/usr/bin/env python

import gtk

distributions = ["Ubuntu", "Debian", "Sabayon", "Fedora", "Arch", "Mint", "Slackware", "Mandriva", "Sidux", "Mepis"]

class ComboBoxEntry:
    def __init__(self):
        window = gtk.Window()
        
        liststore = gtk.ListStore(str)    
        for item in distributions:
            liststore.append([item])
        
        cell = gtk.CellRendererText()
        
        comboboxentry = gtk.ComboBoxEntry(liststore)
        comboboxentry.pack_start(cell, True)
        comboboxentry.set_active(0)
        
        window.add(comboboxentry)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        comboboxentry.connect("changed", self.changed_item)
        
        window.show_all()

    def changed_item(self, widget):
        print "ComboBoxEntry item was changed to %s" % widget.get_active_text()

ComboBoxEntry()
gtk.main()
