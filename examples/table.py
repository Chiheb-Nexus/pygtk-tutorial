#!/usr/bin/env python

import gtk

class Table:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 150)
        table = gtk.Table(3, 3, True)
        
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        button3 = gtk.Button("Button 3")
        button4 = gtk.Button("Button 4")
        button5 = gtk.Button("Button 5")
        
        window.add(table)
        table.attach(button1, 0, 1, 0, 1)
        table.attach(button2, 1, 3, 0, 1)
        table.attach(button3, 0, 1, 1, 3)
        table.attach(button4, 1, 3, 1, 2)
        table.attach(button5, 1, 2, 2, 3)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.show_all()

Table()
gtk.main()
