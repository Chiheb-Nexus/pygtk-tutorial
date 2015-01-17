#!/usr/bin/env python

import gtk

class LinkButton:
    def __init__(self):
        window = gtk.Window()
        linkbutton = gtk.LinkButton("http://www.learnpygtk.org/", "Link Button")

        window.connect("destroy", lambda w: gtk.main_quit())
            
        window.add(linkbutton)
        window.show_all()

LinkButton()
gtk.main()
