#!/usr/bin/env python

import gtk

class Expander:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        label = gtk.Label("Expander")
        expander = gtk.Expander(None)
        expander.set_label_widget(label)

        window.connect("destroy", lambda w: gtk.main_quit())
        expander.connect("notify::expanded", self.expanded)
        
        window.add(expander)
        window.show_all()

    def expanded(self, expander, parameter):
        if expander.get_expanded():
            label = gtk.Label("Label")
            label.set_size_request(200, 100)
            expander.add(label)
            label.show()
        else:
            expander.remove(expander.child)
            expander.get_parent().resize(200, 1)
        
        print "The Expander is currently %s" % ("closed", "open")[expander.get_expanded()]

Expander()
gtk.main()
