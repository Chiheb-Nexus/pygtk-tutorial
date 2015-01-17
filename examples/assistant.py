#!/usr/bin/env python

import gtk

class Assistant:
    def __init__(self):        
        assistant = gtk.Assistant()
        
        assistant.connect("apply", self.button_pressed, "Apply")
        assistant.connect("cancel", self.button_pressed, "Cancel")
        
        vbox = gtk.VBox()
        vbox.set_border_width(5)
        page = assistant.append_page(vbox)
        assistant.set_page_title(vbox, "Page 1: Starting Out")
        assistant.set_page_type(vbox, gtk.ASSISTANT_PAGE_INTRO)
        label = gtk.Label("This is an example label within an Assistant. The Assistant is used to guide a user through configuration of an application.")
        label.set_line_wrap(True)
        vbox.pack_start(label, True, True, 0)
        assistant.set_page_complete(vbox, True)
        
        vbox = gtk.VBox()
        vbox.set_border_width(5)
        assistant.append_page(vbox)
        assistant.set_page_title(vbox, "Page 2: Moving On...")
        assistant.set_page_type(vbox, gtk.ASSISTANT_PAGE_CONTENT)
        label = gtk.Label("This is an example of a label and button within a page. This is a content page primarily used to display options to the end user.")
        label.set_line_wrap(True)
        button = gtk.Button("Button Example")
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(button, False, False, 0)
        assistant.set_page_complete(vbox, True)
        
        vbox = gtk.VBox()
        vbox.set_border_width(5)
        assistant.append_page(vbox)
        assistant.set_page_title(vbox, "Page 3: The Finale")
        assistant.set_page_type(vbox, gtk.ASSISTANT_PAGE_CONFIRM)
        label = gtk.Label("This is the final page of the Assistant widget. It would be used to confirm the preferences we have set in the previous pages.")
        label.set_line_wrap(True)
        vbox.pack_start(label, True, True, 0)
        assistant.set_page_complete(vbox, True)
        
        assistant.show_all()
    
    def button_pressed(self, assistant, button):
        print "%s button pressed" % button
        gtk.main_quit()

Assistant()
gtk.main()
