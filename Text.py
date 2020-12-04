from pygame import font as pyfont

class Text:
    def __init__(self, gui, position, body, font, size, colour):
        self.position = position
        self.font = pyfont.SysFont(font, size)
        self.body = body
        self.textColour = colour
        self.textDimensions = self.font.size(body)
        self.gui = gui

    def Draw(self):
        renderedText = self.font.render(self.body, True, self.textColour)
        x = self.position[0] * self.gui.size[0]
        y = self.position[1] * self.gui.size[1]
        self.gui.display.blit(renderedText, (x, y))
