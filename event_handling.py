#Let us write a program to quit the program when we click the X button on the game screen. This is done by event Handling.


import pygame
pygame.init()
gameDisplay = pygame.display.set_mode((1280,1024))
pygame.display.set_caption('Hello Wormy')

pygame.display.update()

gameExit = False                                     # we are initialising the quit to be false

while not gameExit:
	for event in pygame.event.get():             #get all the events in the module
		if event.type == pygame.QUIT:        #if the event is QUIT then make the variable gameExit = TRUE
			gameExit = True

pygame.quit()
quit()



