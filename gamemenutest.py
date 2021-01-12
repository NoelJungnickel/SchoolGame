import pygame

winName = "Start"

pygame.display.set_caption(winName)
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

bg = pygame.image.load("Steine.png")

class GameWindow():
    def __init__(self):
        pygame.font.init()

        self.win = win
        self.winName = winName
        self.winWidth = 1920
        self.winHeight = 1080
        self.run = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.startButtonWidth = 200
        self.startButtonHeight = 50
        self.keybindButtonWidth = 200
        self.keybindButtonHeight = 50
        self.exitButtonWidth = 200
        self.exitButtonHeight = 50
        self.mainFont = pygame.font.SysFont('comicsans', 50)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.startButtonColor = (36, 36, 36)
        self.keybindButtonColor = (36, 36, 36)
        self.exitButtonColor = (36, 36, 36)
        self.backButtonColor = (36, 36, 36)
        self.showStartButton = True
        self.showKeyButton = True
        self.showExitButton = True
        self.showRand = True
        self.showBackButton = True

    def mainloop(self):
        while self.run:

            self.clock.tick(self.FPS)
            self.startWin()
            self.button()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        
    def startWin(self):
        #self.win.fill(self.black)

        if self.showExitButton:
            self.exitButton = pygame.draw.rect(self.win, self.exitButtonColor, ((self.winWidth - self.exitButtonWidth)/2, (self.winHeight - self.exitButtonHeight)/2, self.exitButtonWidth, self.exitButtonHeight))
            self.exitLabel = self.mainFont.render("Exit", 1, (255, 255, 255))
            self.win.blit(self.exitLabel, (self.winWidth/2 - self.exitLabel.get_rect().size[0]/2, self.winHeight/2 - self.exitLabel.get_rect().size[1]/2))

        if self.showKeyButton:
            self.keybindButton = pygame.draw.rect(self.win, self.keybindButtonColor, ((self.winWidth - self.keybindButtonWidth)/2, (self.winHeight - self.keybindButtonHeight)/2 - self.exitButtonHeight - 20, self.keybindButtonWidth, self.keybindButtonHeight))
            self.keybindLabel = self.mainFont.render("Keybinds", 1, (255, 255, 255))
            self.win.blit(self.keybindLabel, (self.winWidth/2 - self.keybindLabel.get_rect().size[0]/2, (self.winHeight/2 - self.keybindLabel.get_rect().size[1]/2) - self.exitButtonHeight - 20))
        
        if self.showStartButton:
            self.startButton = pygame.draw.rect(self.win, self.startButtonColor, ((self.winWidth - self.startButtonWidth)/2, (self.winHeight - self.startButtonHeight)/2 - self.exitButtonHeight - self.keybindButtonHeight - 40, self.startButtonWidth, self.startButtonHeight))
            self.startLabel = self.mainFont.render("Start", 1, (255, 255, 255))
            self.win.blit(self.startLabel, (self.winWidth/2 - self.startLabel.get_rect().size[0]/2, (self.winHeight/2 - self.startLabel.get_rect().size[1]/2) - self.exitButtonHeight - self.keybindButtonHeight - 40))
        
        if self.showRand:
            self.rand = pygame.draw.rect(self.win, self.blue,(0, 0, self.winWidth, self.winHeight), 20)

        if not self.showBackButton:
            self.backButton = pygame.draw.rect(self.win, self.backButtonColor, (40, self.winHeight - self.exitButtonHeight - 40, self.exitButtonWidth, self.exitButtonHeight))
            self.backLabel = self.mainFont.render("Back", 1, (255, 255, 255))
            self.win.blit(self.backLabel, (self.exitLabel.get_rect().size[0]/2 + 65, self.winHeight - self.exitLabel.get_rect().size[1]/2 - 65))

        pygame.display.update()

    def keyWin(self):
        self.exitButton = pygame.draw.rect(self.win, self.exitButtonColor, (self.winWidth - self.exitButtonWidth - 40, self.winHeight - self.exitButtonHeight - 40, self.exitButtonWidth, self.exitButtonHeight))
        self.exitLabel = self.mainFont.render("Exit", 1, (255, 255, 255))
        self.win.blit(self.exitLabel, (self.winWidth - self.exitLabel.get_rect().size[0]/2 - 135, self.winHeight - self.exitLabel.get_rect().size[1]/2 - 65))

        if self.exitButton.collidepoint(self.mousePos):
            self.exitButtonColor = self.red
        else:
            self.exitButtonColor = (36, 36, 36)

    def button(self):
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
            self.showRand = False

GameWindow().mainloop()

