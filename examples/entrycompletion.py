#!/usr/bin/env python

import gtk

distributions = ["Ubuntu", "Debian", "Sabayon", "Fedora", "Arch", "Mint", "Slackware", "Mandriva", "Sidux", "Mepis"]

class EntryCompletion:
    def __init__(self):
        window = gtk.Window()
        
        liststore = gtk.ListStore(str)
        for item in distributions:
            liststore.append([item])
        
        self.completion = gtk.EntryCompletion()
        self.completion.set_model(liststore)
        self.completion.set_text_column(0)

        comboboxentry = gtk.Entry()
        comboboxentry.set_completion(self.completion)
        
        window.connect("destroy", lambda w: gtk.main_quit())

        window.add(comboboxentry)
        
        window.show_all()

EntryCompletion()
gtk.main()
