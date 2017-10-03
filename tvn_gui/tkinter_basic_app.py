from tkinter import *

# Create a tkinter application window called "app"
app = Tk()
# Give the window a name
app.title("My application")
# Provide window coordinates and size values
app.geometry('405x100+200+100')

# Add a button to the window and give it some text and width values
b1 = Button(app, text = "Click me!", width = 10)
# The pack() method links the newly created button to the existing window
b1.pack()

# Start the tkinter event loop
app.mainloop()
