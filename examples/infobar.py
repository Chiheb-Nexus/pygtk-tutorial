#!/usr/bin/env python

import gtk

class InfoBar:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 5)

        label = gtk.Label("InfoBar Example")

        self.infobar = gtk.InfoBar()
        content = self.infobar.get_content_area()
        content.add(label)

        button_info = gtk.Button("Info")
        button_warning = gtk.Button("Warning")
        button_question = gtk.Button("Question")
        button_error = gtk.Button("Error")

        window.connect("destroy", lambda w: gtk.main_quit())
        button_info.connect("clicked", self.infobar_type, gtk.MESSAGE_INFO)
        button_warning.connect("clicked", self.infobar_type, gtk.MESSAGE_WARNING)
        button_question.connect("clicked", self.infobar_type, gtk.MESSAGE_QUESTION)
        button_error.connect("clicked", self.infobar_type, gtk.MESSAGE_ERROR)
        self.infobar.connect("response", self.infobar_response)

        window.add(vbox)
        vbox.pack_start(self.infobar)
        vbox.pack_start(hbox, False, False, 0)
        hbox.pack_start(button_info)
        hbox.pack_start(button_warning)
        hbox.pack_start(button_question)
        hbox.pack_start(button_error)
        
        window.show_all()

    def infobar_type(self, widget, type):
        self.infobar.set_message_type(type)
        self.infobar.show()

    def infobar_response(self, widget, event):
        self.infobar.hide()

InfoBar()
gtk.main()
