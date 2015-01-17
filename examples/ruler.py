#!/usr/bin/env python

import gtk

class Ruler:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(400, 400)
        
        table = gtk.Table(2, 2, False)
        drawingarea = gtk.DrawingArea()
        drawingarea.set_size_request(400, 400)
        drawingarea.set_events(gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.POINTER_MOTION_HINT_MASK)
        hruler = gtk.HRuler()
        hruler.set_range(0, 10, 0, 0)
        vruler = gtk.VRuler()
        vruler.set_range(0, 10, 0, 0)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        drawingarea.connect_object("motion-notify-event", self.motion_notify, hruler)
        drawingarea.connect_object("motion-notify-event", self.motion_notify, vruler)
        
        window.add(table)
        table.attach(hruler, 1, 2, 0, 1, gtk.EXPAND | gtk.FILL, gtk.FILL)
        table.attach(vruler, 0, 1, 1, 2, gtk.FILL, gtk.EXPAND | gtk.FILL)
        table.attach(drawingarea, 1, 2, 1, 2, gtk.FILL, gtk.FILL)
        
        window.show_all()
        
    def motion_notify(self, ruler, event):
        ruler.emit("motion-notify-event", event)

Ruler()
gtk.main()
