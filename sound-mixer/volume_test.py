import pygame.mixer
from time import sleep

mixer = pygame.mixer
mixer.init()

track = mixer.Sound("50459_M_RED_Nephlimizer.wav")
print("Play it LOUD, man!")
track.play(loops=-1)
# Set the volume to a LOUD setting
track.set_volume(0.9)
sleep(2)
print("Softly does it... ")
track.set_volume(0.1)
sleep(2)
track.stop()
