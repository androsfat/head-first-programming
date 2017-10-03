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


# This function either plays or stops the track based on the state of the checkbox
def track_toggle():
    if track_playing.get() == 1:
        track.play(loops=-1)
    else:
        track.stop()

# Lookup the track file
track = mixer.Sound(sound_file)

track_playing = IntVar()


# This function will stop all necessary job before shutdown
def shutdown():
    if askokcancel(title="Are you sure?", message="Do you really want to quit?"):
        # Stop any paying tracks
        track.stop()
        # Close the application
        app.destroy()

track_button = Checkbutton(app, variable=track_playing, command=track_toggle, text=sound_file)
track_button.pack()

app.protocol("WM_DELETE_WINDOW", shutdown)

# Start the GUI event loop
app.mainloop()
