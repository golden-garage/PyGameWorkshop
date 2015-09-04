
import pygame #This is to import the pygame library

pygame.init()  #we need to initialise all the modules in pygame

gameDisplay = pygame.display.set_mode((1280,1024)) #gameDisplay is the name of the surface we create. The resolution of the screen is 1280x1024.

pygame.display.set_caption('Hello Wormy') #We want to set the caption as Hello Wormy
pygame.display.update() #the changes in the frame can be shown only if it is updated. Hence we update the screen

pygame.quit() #Quits the pygame module
quit() #quits python

