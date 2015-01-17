#!/usr/bin/env python

import gtk

class TextViewBasic:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(-1, 350)
        
        vbox = gtk.VBox(False, 5)
        scrolledwindow = gtk.ScrolledWindow()
        scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        table = gtk.Table(3, 3, False)
        
        self.textview = gtk.TextView()
        textbuffer = self.textview.get_buffer()
        
        check_editable = gtk.CheckButton("Editable")
        check_editable.set_active(True)
        check_cursor = gtk.CheckButton("Cursor Visible")
        check_cursor.set_active(True)
        radio_wrapnone = gtk.RadioButton(None, "No Wrapping")
        radio_wrapchar = gtk.RadioButton(radio_wrapnone, "Character Wrapping")
        radio_wrapword = gtk.RadioButton(radio_wrapnone, "Word Wrapping")
        radio_justifyleft = gtk.RadioButton(None, "Justify Left")
        radio_justifycenter = gtk.RadioButton(radio_justifyleft, "Justify Center")
        radio_justifyright = gtk.RadioButton(radio_justifyleft, "Justify Right")
        
        table.attach(check_editable, 0, 1, 0, 1)
        table.attach(check_cursor, 0, 1, 1, 2)
        table.attach(radio_wrapnone, 1, 2, 0, 1)
        table.attach(radio_wrapchar, 1, 2, 1, 2)
        table.attach(radio_wrapword, 1, 2, 2, 3)
        table.attach(radio_justifyleft, 2, 3, 0, 1)
        table.attach(radio_justifycenter, 2, 3, 1, 2)
        table.attach(radio_justifyright, 2, 3, 2, 3)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        check_editable.connect("toggled", self.toggle_editable)
        check_cursor.connect("toggled", self.toggle_cursor)
        radio_wrapnone.connect("toggled", self.configure_wrap, gtk.WRAP_NONE)
        radio_wrapchar.connect("toggled", self.configure_wrap, gtk.WRAP_CHAR)
        radio_wrapword.connect("toggled", self.configure_wrap, gtk.WRAP_WORD)
        radio_justifyleft.connect("toggled", self.configure_justification, gtk.JUSTIFY_LEFT)
        radio_justifycenter.connect("toggled", self.configure_justification, gtk.JUSTIFY_CENTER)
        radio_justifyright.connect("toggled", self.configure_justification, gtk.JUSTIFY_RIGHT)
        
        window.add(vbox)
        vbox.pack_start(scrolledwindow, True, True, 0)
        vbox.pack_end(table, False, False, 0)
        scrolledwindow.add(self.textview)
        
        window.show_all()
    
    def toggle_editable(self, widget):
        self.textview.set_editable(widget.get_active())
    
    def toggle_cursor(self, widget):
        self.textview.set_cursor_visible(widget.get_active())
    
    def configure_wrap(self, widget, wrap):
        self.textview.set_wrap_mode(wrap)
    
    def configure_justification(self, widget, justification):
        self.textview.set_justification(justification)

TextViewBasic()
gtk.main()
