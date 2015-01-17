#!/usr/bin/env python

import gtk

class AboutDialog():
    def __init__(self):
        aboutdialog = gtk.AboutDialog()
        aboutdialog.set_name("PyGTK Tutorial")
        aboutdialog.set_version("0.00")
        aboutdialog.set_comments("New PyGTK Tutorial featuring updated widgets and methods")
        aboutdialog.set_website("http://www.learnpygtk.org/")
        aboutdialog.set_website_label("Learn PyGTK Website")
        aboutdialog.set_authors(["Andrew Steele"])

        aboutdialog.run()
        aboutdialog.destroy()

AboutDialog()
