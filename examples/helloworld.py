# Invoke the Python interpreter. This should be the first line in all Python programs.
#!/usr/bin/env python

# Import the PyGTK bindings so that we can access them
import gtk

# Define our class named HelloWorld
class HelloWorld:
    # Create a function to handle quitting the application
    def close(self, widget):
        # Exit the GTK main loop
        gtk.main_quit()
    
    # Create a function to allow printing "Hello World" to the shell
    def print_hello_world(self, widget):
        print "Hello World"
    
    def __init__(self):
        # Create our window
        window = gtk.Window()
        # Create our button with appropriate text label
        button = gtk.Button("Click Here")
        
        # Connect the window destroy event to the close function
        # This allows the application to exit when the X button is clicked
        window.connect("destroy", self.close)
        # Connect the button to the print function
        # When clicked, Python will call the print_hello_world function
        button.connect("clicked", self.print_hello_world)
        
        # Add the button to the window
        window.add(button)
        # Use show_all() to display all widgets on the window
        window.show_all()

# Run the HelloWorld class
HelloWorld()
# This is the GTK main loop. Once the HelloWorld class has run, control will sleep
# here until an event is triggered. 
gtk.main()
