from tkinter import *
from sound_panel import *
# from tkinter.messagebox import askokcancel
import pygame.mixer
import os

app = Tk()
app.title("Sound Mix")
# app.geometry('300x100+200+100')

# Start the sound system
mixer = pygame.mixer
mixer.init()

# Get names of all files in current directory
dirList = os.listdir(".")
# Take each of the filenames...
for fname in dirList:
    # ... an if it ends in ".wav"
    if fname.endswith(".wav"):
        # Create the panel and add it to the GUI
        panel = SoundPanel(app, mixer, fname)
        panel.pack()


# This function will stop all necessary jobs before shutdown
def shutdown():
    # if askokcancel(title="Are you sure?", message="Do you really want to quit?"):
    # Stop any paying tracks
    mixer.stop()
    # Close the application
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

# Start the GUI event loop
app.mainloop()
