#!/usr/bin/env python

import gtk

class MessageDialog:
    def __init__(self):
        self.window = gtk.Window()
        
        vbox = gtk.VBox(True, 5)
        
        button_info = gtk.Button("Information")
        button_error = gtk.Button("Error")
        button_warning = gtk.Button("Warning")
        button_question = gtk.Button("Question")
        
        self.window.connect("destroy", lambda w: gtk.main_quit())
        button_info.connect("clicked", self.information_message)
        button_error.connect("clicked", self.error_message)
        button_warning.connect("clicked", self.warning_message)
        button_question.connect("clicked", self.question_message)
        
        self.window.add(vbox)
        vbox.pack_start(button_info)
        vbox.pack_start(button_error)
        vbox.pack_start(button_warning)
        vbox.pack_start(button_question)
        
        self.window.show_all()
    
    def information_message(self, widget):
        messagedialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, "Download of file has completed.")
        messagedialog.run()
        messagedialog.destroy()
    
    def error_message(self, widget):
        messagedialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_ERROR, gtk.BUTTONS_CANCEL, "File could not be accessed. Read operation cancelled.")
        messagedialog.run()
        messagedialog.destroy()
    
    def warning_message(self, widget):
        messagedialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_WARNING, gtk.BUTTONS_OK_CANCEL, "Folder merge conflict while writing.")
        messagedialog.run()
        messagedialog.destroy()
    
    def question_message(self, widget):
        messagedialog = gtk.MessageDialog(self.window, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Continue with file conversion operation?")
        messagedialog.run()
        messagedialog.destroy()

MessageDialog()
gtk.main()
