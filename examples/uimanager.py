#!/usr/bin/env python

import gtk

class UIManager:
    interface = """
    <ui>
        <menubar name="MenuBar">
            <menu action="File">
                <menuitem action="New"/>
                <menuitem action="Open"/>
                <menuitem action="Save"/>
                <menuitem action="Quit"/>
            </menu>
            <menu action="Edit">
                <menuitem action="Preferences"/>
            </menu>
            <menu action="Help">
                <menuitem action="About"/>
            </menu>
        </menubar>
    </ui>
    """

    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        vbox = gtk.VBox()
        
        uimanager = gtk.UIManager()
        accelgroup = uimanager.get_accel_group()
        window.add_accel_group(accelgroup)
        
        self.actiongroup = gtk.ActionGroup("uimanager")
        self.actiongroup.add_actions([
                                    ("New", gtk.STOCK_NEW, "_New", None, "Create a New Document"),
                                    ("Open", gtk.STOCK_OPEN, "_Open", None, "Open an Existing Document"),
                                    ("Save", gtk.STOCK_SAVE, "_Save", None, "Save the Current Document"),
                                    ("Quit", gtk.STOCK_QUIT, "_Quit", None, "Quit the Application", lambda w: gtk.main_quit()),
                                    ("File", None, "_File"), 
                                    ("Preferences", gtk.STOCK_PREFERENCES, "_Preferences", None, "Edit the Preferences"),
                                    ("Edit", "None", "_Edit"),
                                    ("About", gtk.STOCK_ABOUT, "_About", None, "Open the About dialog"),
                                    ("Help", "None", "_Help")
                                    ])
        
        uimanager.insert_action_group(self.actiongroup, 0)
        uimanager.add_ui_from_string(self.interface)
        
        menubar = uimanager.get_widget("/MenuBar")
        vbox.pack_start(menubar, False)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(vbox)
        window.show_all()

UIManager()
gtk.main()
