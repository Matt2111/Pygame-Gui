from pygame.draw import rect
from pygame import font as pyfont

class Rectangle:
    def __init__(self, gui, position, size, borderWidth, borderCol, backgroundCol):
        self.position, self.size = position, size
        self.borderWidth = borderWidth
        self.colour, self.bgCol, self.textColour = borderCol, backgroundCol, None
        self.gui = gui
        self.font, self.textDimensions, self.body = None, None, None
        self.textPos = None

    def Draw(self):
        if self.bgCol is not None:
            rect(self.gui.display, self.bgCol, (self.position[0] * self.gui.size[0],
                                                self.position[1] * self.gui.size[1],
                                                self.size[0] * self.gui.size[0],
                                                self.size[1] * self.gui.size[1]), 0)
        rect(self.gui.display, self.colour, (self.position[0] * self.gui.size[0],
                                             self.position[1] * self.gui.size[1],
                                             self.size[0] * self.gui.size[0],
                                             self.size[1] * self.gui.size[1]), self.borderWidth)

        if self.body is not None:
            if self.textDimensions[0] + self.borderWidth < self.size[0] * self.gui.size[0] and self.textDimensions[1] + self.borderWidth < self.size[1] * self.gui.size[1]:
                renderedText = self.font.render(self.body, True, self.textColour)
                if self.textPos[0] == 1:
                    x = (((self.size[0] * self.gui.size[0]) - self.textDimensions[0]) / 2) + (self.position[0] * self.gui.size[0])
                elif self.textPos[0] == 0:
                    x = (self.position[0] * self.gui.size[0]) + self.borderWidth
                elif self.textPos[0] == 2:
                    x = ((self.position[0] * self.gui.size[0]) + self.size[0] * self.gui.size[0]) - self.borderWidth - self.textDimensions[0]
                else:
                    return
                if self.textPos[1] == 1:
                    y = (((self.size[1] * self.gui.size[1]) - self.textDimensions[1]) / 2) + (self.position[1] * self.gui.size[1])
                elif self.textPos[1] == 0:
                    y = (self.position[1] * self.gui.size[1]) + self.borderWidth
                elif self.textPos[1] == 2:
                    y = ((self.position[1] * self.gui.size[1]) + self.size[1] * self.gui.size[1]) - self.borderWidth - self.textDimensions[1]
                else:
                    return
                self.gui.display.blit(renderedText, (x, y))

    def AttachText(self, body, font, size, colour, pos=(1, 1)):
        self.font = pyfont.SysFont(font, size)
        self.body = body
        self.textColour = colour
        self.textDimensions = self.font.size(body)
        self.textPos = tuple(pos)
