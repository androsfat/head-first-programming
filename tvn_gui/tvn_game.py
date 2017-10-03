from tkinter import *

import pygame.mixer


def play_correct_sound():
    num_good.set(num_good.get() + 1)
    correct_s.play()


def play_wrong_sound():
    num_bad.set(num_bad.get() + 1)
    wrong_s.play()

# Create a tkinter application window called "app"
app = Tk()
# Give the window a name
app.title("TVN Game Show")
# Provide window coordinates and size values
app.geometry('300x110+200+100')

# Initialise the sound system
sounds = pygame.mixer
sounds.init()

# Load the required sounds
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

# Create 2 IntVars: one to count correct and one to count wrong answers
num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)

# Display a message that tell the host what to do
lab = Label(app, text='When you are ready, click the buttons!', height=3)
lab.pack()

# Create two labels to hold each counter and connect them to the relevant IntVars
lab1 = Label(app, textvariable=num_good)
lab1.pack(side='left')

lab2 = Label(app, textvariable=num_bad)
lab2 .pack(side='right')

# Add a button to the window and give it some text and width value
b1 = Button(app, text="Correct!", width=10, command=play_correct_sound)
# The pack() method links the newly created button to the existing window
b1.pack(side="left", padx=10, pady=10)

b2 = Button(app, text="Wrong!", width=10, command=play_wrong_sound)
b2.pack(side="right", padx=10, pady=10)

# Start the tkinter event loop
app.mainloop()

# num_correct = str(number_correct) + " were correctly answered."
# number_wrong = str(number_wrong) + " were answered incorrectly."
