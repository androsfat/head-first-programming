from tkinter import *
from tkinter.messagebox import askokcancel

import pygame.mixer

# Create the GUI application window
app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

# Identify DJ's track
sound_file = "50459_M_RED_Nephlimizer.wav"
# Start the sound system
mixer = pygame.mixer
mixer.init()


# This function will respond to the Start button-click event
def track_start():
    # the "loops=-1" parameter to "play()" repeats the track until you stop it
    track.play(loops=-1)


# This function will respond to the Stop button-click event
def track_stop():
    track.stop()


# This function will stop all necessary job before shutdown
def shutdown():
    if askokcancel(title="Are you sure?", message="Do you really want to quit?"):
        # Stop any paying tracks
        track_stop()
        # Close the application
        app.destroy()

# Lookup the track file
track = mixer.Sound(sound_file)

# Create start and stop buttons and connect them to their event handlers
start_button = Button(app, command=track_start, text="Start")
start_button.pack(side=LEFT)
stop_button = Button(app, command=track_stop, text="Stop")
stop_button.pack(side=RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)

# Start the GUI event loop
app.mainloop()
