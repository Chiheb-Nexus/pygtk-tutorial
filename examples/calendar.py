#!/usr/bin/env python

import gtk

class Calendar:
    def __init__(self):
        window = gtk.Window()
        window.set_border_width(5)
        
        hbox = gtk.HBox(False, 5)
        vbox = gtk.VBox(False, 5)
        
        self.calendar = gtk.Calendar()
        self.calendar.set_property("show-heading", False)
        self.calendar.set_property("show-day-names", False)
        
        check_heading = gtk.CheckButton("Show Month/Year Heading")
        check_daynames = gtk.CheckButton("Show Day Names")
        check_weeknumbers = gtk.CheckButton("Display Week Numbers")
        check_nochange = gtk.CheckButton("Prevent Month/Year Changes")

        window.connect("destroy", lambda w: gtk.main_quit())
        self.calendar.connect("day-selected", self.date)
        check_heading.connect("toggled", self.heading_toggle)
        check_daynames.connect("toggled", self.daynames_toggle)
        check_weeknumbers.connect("toggled", self.weeknumbers_toggle)
        check_nochange.connect("toggled", self.nochange_toggle)

        window.add(hbox)
        hbox.pack_start(self.calendar, False, False, 0)
        hbox.pack_start(vbox, False, False, 0)
        vbox.pack_start(check_heading, False, False, 0)
        vbox.pack_start(check_daynames, False, False, 0)
        vbox.pack_start(check_weeknumbers, False, False, 0)
        vbox.pack_start(check_nochange, False, False, 0)
        
        window.show_all()
    
    def date(self, widget):
        date = self.calendar.get_date()
        year, month, day = date
        
        print day, "/", month, "/", year
    
    def heading_toggle(self, widget):
        self.calendar.set_property("show-heading", widget.get_active())
    
    def daynames_toggle(self, widget):
        self.calendar.set_property("show-day-names", widget.get_active())
    
    def weeknumbers_toggle(self, widget):
        self.calendar.set_property("show-week-numbers", widget.get_active())
    
    def nochange_toggle(self, widget):
        self.calendar.set_property("no-month-change", widget.get_active())

Calendar()
gtk.main()
