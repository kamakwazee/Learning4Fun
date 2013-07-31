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
    def checkDisplay(self):
        if self.correctDisplaying:
            self.displayInc += 1
            if self.displayInc >= 150:
                self.displayInc = 0
                self.correctDisplaying = False
                self.drawQuestion()
        elif self.wrongDisplaying:
            self.displayInc += 1
            if self.displayInc >= 150:
                self.displayInc = 0
                self.wrongDisplaying = False
                self.drawQuestion()
    def checkHover(self):
        xco, yco = pygame.mouse.get_pos(0)
        if xco in range(self.a1_x,self.a1_x+72) and yco in range(self.a1_y,self.a1_y+72):
            self.a1_hover = True
            self.a2_hover = False
            self.a3_hover = False
            self.a4_hover = False
        elif xco in range(self.a2_x,self.a2_x+72) and yco in range(self.a2_y,self.a2_y+72):
            self.a1_hover = False
            self.a2_hover = True
            self.a3_hover = False
            self.a4_hover = False
        elif xco in range(self.a3_x,self.a3_x+72) and yco in range(self.a3_y,self.a3_y+72):
            self.a1_hover = False
            self.a2_hover = False
            self.a3_hover = True
            self.a4_hover = False
        elif xco in range(self.a4_x,self.a4_x+72) and yco in range(self.a4_y,self.a4_y+72):
            self.a1_hover = False
            self.a2_hover = False
            self.a3_hover = False
            self.a4_hover = True
        else:
            self.a1_hover = False
            self.a2_hover = False
            self.a3_hover = False
            self.a4_hover = False
    def updateScreen(self):
        self.screen.fill(self.black)
        if self.correctDisplaying == False and self.wrongDisplaying == False:
            self.screen.blit(self.question,(self.q_x,self.q_y))
            self.screen.blit(self.ans1,(self.a1_x,self.a1_y))
            self.screen.blit(self.ans2,(self.a2_x,self.a2_y))
            self.screen.blit(self.ans3,(self.a3_x,self.a3_y))
            self.screen.blit(self.ans4,(self.a4_x,self.a4_y))
            if(self.a1_hover):
                self.screen.blit(self.a1h,(self.a1_x,self.a1_y))
            elif(self.a2_hover):
                self.screen.blit(self.a2h,(self.a2_x,self.a2_y))
            elif(self.a3_hover):
                self.screen.blit(self.a3h,(self.a3_x,self.a3_y))
            elif(self.a4_hover):
                self.screen.blit(self.a4h,(self.a4_x,self.a4_y))
        else:
            if self.correctDisplaying:
                correct = self.cwFont.render("CORRECT!", 1, self.lime)
                self.screen.blit(correct, (self.q_x, self.q_y))
            elif self.wrongDisplaying:
                wrong = self.cwFont.render("WRONG!", 1, self.red)
                self.screen.blit(wrong, (self.q_x, self.q_y))
    def randomLetter(self, *exclusion):
        if exclusion is None:
            return self.abc[randint(0,len(self.abc)-1)]
        else:
            l = self.abc[randint(0,len(self.abc)-1)]
            for e in exclusion:
                if l == e:
                    return self.randomLetter(exclusion)
            return l
    def drawQuestion(self):
        self.letter = self.randomLetter()
        self.question = self.font.render("Which is the letter " + self.letter.capitalize() + "?", 1, self.white)
        self.answerPos = randint(1,4)
        if self.answerPos == 1:
            l1 = self.letter
            l2 = self.randomLetter(l1)
            l3 = self.randomLetter(l1,l2)
            l4 = self.randomLetter(l1,l2,l3)
        elif self.answerPos == 2:
            l2 = self.letter
            l1 = self.randomLetter(l2)
            l3 = self.randomLetter(l1,l2)
            l4 = self.randomLetter(l1,l2,l3)
        elif self.answerPos == 3:
            l3 = self.letter
            l1 = self.randomLetter(l3)
            l2 = self.randomLetter(l1,l3)
            l4 = self.randomLetter(l1,l2,l3)
        elif self.answerPos == 4:
            l4 = self.letter
            l1 = self.randomLetter(l4)
            l2 = self.randomLetter(l1,l4)
            l3 = self.randomLetter(l1,l2,l4)
        self.answers = [l1,l2,l3,l4]
        self.answerIndex = self.answerPos-1
        self.ans1 = self.font.render(self.answers[0].capitalize(), 1, self.white)
        self.ans2 = self.font.render(self.answers[1].capitalize(), 1, self.white)
        self.ans3 = self.font.render(self.answers[2].capitalize(), 1, self.white)
        self.ans4 = self.font.render(self.answers[3].capitalize(), 1, self.white)
        self.a1h = self.font.render(self.answers[0].capitalize(), 1, self.yellow)
        self.a2h = self.font.render(self.answers[1].capitalize(), 1, self.yellow)
        self.a3h = self.font.render(self.answers[2].capitalize(), 1, self.yellow)
        self.a4h = self.font.render(self.answers[3].capitalize(), 1, self.yellow)
    def declareVar(self):
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.yellow = (255,255,0)
        self.lime = (0,255,0)
        self.red = (255,0,0)
        root = Tk()
        self.window_w = root.winfo_screenwidth()
        self.window_h = root.winfo_screenheight()
        self.screen = pygame.display.set_mode((self.window_w,self.window_h),FULLSCREEN,0)
        self.abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','l','o','p','q','r','s','t','u','v','w','x','y','z']
        self.answers = []
        self.answerPos = 0
        self.answerIndex = 0
        self.correctDisplaying = False
        self.wrongDisplaying = False
        #Dynamic positioning
        #Possibly needs changing
        self.q_x = int(round(self.window_w * .1))
        self.q_y = int(round(self.window_h * .1))
        self.a1_x = int(round(self.window_w * .1))
        self.a1_y = int(round(self.window_h * .2))
        self.a2_x = int(round(self.window_w * .55))
        self.a2_y = int(round(self.window_h * .2))
        self.a3_x = int(round(self.window_w * .1))
        self.a3_y = int(round(self.window_h * .6))
        self.a4_x = int(round(self.window_w * .55))
        self.a4_y = int(round(self.window_h * .6))
        #Hover variables
        self.a1_hover = False
        self.a2_hover = False
        self.a3_hover = False
        self.a4_hover = False
        #font variables
        self.font_size = 72 #Subject to change
        self.font = pygame.font.SysFont("Times New Roman", self.font_size)
        self.cwFont = pygame.font.SysFont("Times New Roman", self.font_size+50)
        self.displayInc = 0
    def events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                xco, yco = event.pos
                if self.correctDisplaying == False and self.wrongDisplaying == False:
                    if xco in range(self.a1_x,self.a1_x+72) and yco in range(self.a1_y,self.a1_y+72):
                        if self.answerPos == 1:
                            self.correctDisplaying = True
                        else:
                            self.wrongDisplaying = True
                    elif xco in range(self.a2_x,self.a2_x+72) and yco in range(self.a2_y,self.a2_y+72):
                        if self.answerPos == 2:
                            self.correctDisplaying = True
                        else:
                            self.wrongDisplaying = True
                    elif xco in range(self.a3_x,self.a3_x+72) and yco in range(self.a3_y,self.a3_y+72):
                        if self.answerPos == 3:
                            self.correctDisplaying = True
                        else:
                            self.wrongDisplaying = True
                    elif xco in range(self.a4_x,self.a4_x+72) and yco in range(self.a4_y,self.a4_y+72):
                        if self.answerPos == 4:
                            self.correctDisplaying = True
                        else:
                            self.wrongDisplaying = True
    def __init__(self):
        pygame.init()
        #Initialize variables
        self.declareVar()
        self.drawQuestion()
        while True:
            self.events()
            self.checkHover()
            self.updateScreen()
            self.checkDisplay()
            pygame.display.flip()

Main()





