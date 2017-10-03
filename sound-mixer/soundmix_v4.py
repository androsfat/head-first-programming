from tkinter import *
from sound_panel import *
# from tkinter.messagebox import askokcancel
import pygame.mixer

app = Tk()
app.title("Sound Mix")
# app.geometry('300x100+200+100')

# Start the sound system
mixer = pygame.mixer
mixer.init()

# Initialise class
panel = SoundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
panel.pack()
panel = SoundPanel(app, mixer, "49119_M_RED_HardBouncer.wav")
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
