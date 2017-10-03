import pygame.mixer
sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass

s = sounds.Sound("heartbeat.wav")
wait_finish(s.play())
s2 = sounds.Sound("buzz.wav")
wait_finish(s2.play())
