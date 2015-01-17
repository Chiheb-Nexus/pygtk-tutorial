#!/usr/bin/env python

import gtk

class Statusbar:
    def __init__(self):
        self.count = 0
    
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 5)
        
        button_push = gtk.Button("Push Message")
        button_pop = gtk.Button("Pop Message")
        self.statusbar = gtk.Statusbar()
        context = self.statusbar.get_context_id("example")

        window.connect("destroy", lambda w: gtk.main_quit())
        button_push.connect("clicked", self.push_message, context)
        button_pop.connect("clicked", self.pop_message, context)

        window.add(vbox)
        vbox.pack_start(hbox, False, False, 0)
        vbox.pack_start(self.statusbar, False, False, 0)
        hbox.pack_start(button_push)
        hbox.pack_start(button_pop)
        window.show_all()
    
    def push_message(self, widget, context):
        self.count += 1
        self.statusbar.push(context, "Message number %s" % str(self.count))
    
    def pop_message(self, widget, context):
        self.statusbar.pop(context)

Statusbar()
gtk.main()
