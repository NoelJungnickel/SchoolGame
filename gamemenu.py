import pygame


winName = "Start"
winWidth = 1600
winHeight = 900


pygame.display.set_caption(winName)
win = pygame.display.set_mode((winWidth, winHeight))
#win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class Font():
    def __init__(self, text, color, x, y):
        pygame.font.init()
        self.mainFont = pygame.font.SysFont('comicsans', 50)

        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.win = win

    def drawLetter(self):
        self.label = self.mainFont.render(self.text, 1, self.color)
        self.win.blit(self.label, (self.x, self.y))

    def getLabelWidth(self):
        return self.labelWidth == self.label.get_rect().size[0]

    def getLabelHeight(self):
        return self.labelHeight == self.label.get_rect().size[1]

class Button():
    def __init__(self, color, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        
    def drawButton(self):
        pygame.draw.rect(self.win, self.color, (self.x, self.y, self.width, self.height))

            
class Window():
    def __init__(self):
        
        self.win = win
        self.winName = winName
        self.run = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.winWidth = winWidth
        self.winHeight = winHeight
        
    def mainloop(self):

        self.createStartscreen()

        while self.run:

            self.clock.tick(self.FPS)
            self.win.fill((0, 0, 0))
            self.placeStartscreen()
            #self.buttonPress()
            self.border()

            pygame.display.update()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
    
    def border(self):
        pygame.draw.rect(self.win, (0, 0, 255), (0, 0, self.winWidth, self.winHeight), 20)

    def createStartscreen(self):
        self.startButton = Button((0, 255, 0), self.winWidth/2 - 100, self.winHeight/2 - 100, 200, 50)
        self.keyButton = Button((0, 0, 255), self.winWidth/2 - 100, self.winHeight/2 - 25, 200, 50)
        self.exitButton = Button((36, 36, 36), self.winWidth/2 - 100, self.winHeight/2 + 50, 200, 50)
        self.exitLabel = Font("EXIT", (255, 255, 255), self.winWidth/2 - 40, self.winHeight/2 + 60)

    def placeStartscreen(self):
        self.startButton.drawButton()
        self.keyButton.drawButton()
        self.exitButton.drawButton()
        self.exitLabel.drawLetter()

    """def buttonPress(self):
        self.mousePos = pygame.mouse.get_pos()
        self.mousePressed = pygame.mouse.get_pressed()
     
        if self.exitButton.collidepoint(self.mousePos):
                self.exitButtonColor = (255, 0, 0)
        else:
            self.exitButtonColor = (36, 36, 36)"""



Window().mainloop()


"""def button(self):
        self.mousePos = pygame.mouse.get_pos()
        self.mousePressed = pygame.mouse.get_pressed() 

        if self.exitButton.collidepoint(self.mousePos):
            self.exitButtonColor = self.red 
        else:
            self.exitButtonColor = (36, 36, 36)

        if self.mousePressed == (1, 0, 0) and self.exitButton.collidepoint(self.mousePos):
            exit()

        if self.keybindButton.collidepoint(self.mousePos):
            self.keybindButtonColor = self.blue
        else:
            self.keybindButtonColor = (36, 36, 36)

        if self.mousePressed == (1, 0, 0) and self.keybindButton.collidepoint(self.mousePos):
            self.win.fill(self.black)
            self.showStartButton = False
            self.showKeyButton = False
            self.showExitButton = False
            self.showBackButton = False
            self.keyWin()

        if self.startButton.collidepoint(self.mousePos):
            self.startButtonColor = self.green
        else:
            self.startButtonColor = (36, 36, 36)

        if self.mousePressed == (1, 0, 0) and self.startButton.collidepoint(self.mousePos):
            self.win.blit(bg, (0, 0))
            self.showStartButton = False
            self.showKeyButton = False
            self.showExitButton = False
            self.showRand = False"""