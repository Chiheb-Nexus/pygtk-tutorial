#!/usr/bin/env python

import gtk

icons = [gtk.STOCK_OPEN, gtk.STOCK_NEW, gtk.STOCK_SAVE, gtk.STOCK_CLOSE, gtk.STOCK_PRINT]

class IconView:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        liststore = gtk.ListStore(gtk.gdk.Pixbuf)
        iconview = gtk.IconView()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        
        for icon in icons:
            pixbuf = iconview.render_icon(icon, gtk.ICON_SIZE_LARGE_TOOLBAR)
            liststore.append([pixbuf])
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(iconview)
        window.show_all()
        
IconView()
gtk.main()
