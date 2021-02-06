

from shapeCreator import Entry, Label, Button, LabelAlt, ButtonAlt

class Screen(): 
    def render(self, win):
        pass

    def checkCollision(self, rect):
        return False


class Screen1(Screen):
    def __init__(self):
        self.label = LabelAlt("1", 500, 500, (255, 0, 0), 200)

    def render(self, win):
        self.label.render(win)



class NotImplemntedScreen(Screen):
    def __init__(self):
        self.label = LabelAlt("NOT IMPLEMENTED YET", 500, 500, (255, 0, 0), 200)

    def render(self, win):
        win.fill((200, 0, 0))
        self.label.render(win)


class Screen2(Screen):
    def __init__(self):
        self.label = LabelAlt("2", 500, 500, (255, 0, 0), 200)
        self.triggerFight = ButtonAlt((255, 255, 255), 600, 600, 80, 50, text = 'FIGHT', textColor = (0, 0, 255), textSize = 50)

    def render(self, win): 
        self.triggerFight.render(win)
        self.label.render(win)
    
    def checkCollision(self, rect):
        return self.triggerFight.checkCollisionRect(rect)
