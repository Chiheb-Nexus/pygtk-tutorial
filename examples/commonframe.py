#!/usr/bin/env python

import gtk

class CommonFrame:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        frame = gtk.Frame()
        frame.set_shadow_type(gtk.SHADOW_NONE)
        label = gtk.Label("<b>Common Frame</b>")
        label.set_use_markup(True)
        frame.set_label_widget(label)
        
        alignment = gtk.Alignment()
        alignment.set_padding(5, 0, 12, 0)
        alignment.set(0.5, 0.5, 1.0, 1.0)
        frame.add(alignment)
        
        label = gtk.Label("Label in Common Frame")
        alignment.add(label)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(frame)
        window.show_all()

CommonFrame()
gtk.main()
