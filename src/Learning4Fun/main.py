#Main File for Learning4Fun
#
#Created and maintained by Kamakwazee Games from Kamakwazee Organizations.
#
#

import pygame, sys, Tkinter, random
from pygame.locals import *
from Tkinter import *
from random import randint

class Main:
    def randomLetter(self, exclusion=None):
        if exclusion is None:
            return self.abc[randint(0,len(self.abc)-1)]
        else:
            l = self.abc[randint(0,len(self.abc)-1)]
            if l == exclusion:
                return self.randomLetter(exclusion)
            else:
                return l
    def drawQuestion(self):
        self.letter = self.randomLetter()
    def declareVar(self):
        self.white = (255,255,255)
        root = Tk()
        self.window_w = root.winfo_screenwidth()
        self.window_h = root.winfo_screenheight()
        self.screen = pygame.display.set_mode((self.window_w,self.window_h),FULLSCREEN,0)
        self.abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
    def events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    def __init__(self):
        pygame.init()
        #Initialize variables
        self.declareVar()
        self.drawQuestion()
        while True:
            self.events()
            pygame.display.flip()

Main()





