#!/usr/bin/env python

import gtk

class SpinButton:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)
        
        adjustment = gtk.Adjustment(0, 0, 100, 1, 10, 0)
        self.spinbutton = gtk.SpinButton(adjustment)
        check_snapticks = gtk.CheckButton("Snap to Ticks")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        check_snapticks.connect("toggled", self.snapticks)
        
        window.add(vbox)
        vbox.pack_start(self.spinbutton, False, False, 0)
        vbox.pack_start(check_snapticks, False, False, 0)
        
        window.show_all()
    
    def snapticks(self, widget):
        self.spinbutton.set_snap_to_ticks(widget.get_active())
        
SpinButton()
gtk.main()
