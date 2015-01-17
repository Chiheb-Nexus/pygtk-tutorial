#!/usr/bin/env python

import gtk

class VolumeButton:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(100, 100)
        volumebutton = gtk.VolumeButton()
        volumebutton.set_value(0.5)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        volumebutton.connect("value-changed", self.value_changed)
        
        window.add(volumebutton)
        window.show_all()

    def value_changed(self, volumebutton, value):
        print "Volume Button is set to %f" % value

VolumeButton()
gtk.main()
