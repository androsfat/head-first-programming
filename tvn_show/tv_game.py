import pygame.mixer

def wait_finish(channel):
    while channel.get_busy():
        pass

# Create a mixer object and initialise the  pygame sound system
sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")


prompt = "Press 1 for Correct, 2 for Wrong, 0 to Quit: "

asked = 0
correct = 0
wrong = 0

choice = input(prompt)
while choice != '0':
    if choice == '1':
        asked = asked + 1
        correct = correct + 1
        wait_finish(correct_s.play())
    elif choice == '2':
        asked = asked + 1
        wrong = wrong + 1
        wait_finish(wrong_s.play())
    choice = input(prompt)

print("You asked %s questions" % str(asked))
print("%s were correctly answered" % str(correct))
print("%s were answered incorrectly" % str(wrong))
