from pygame.draw import line

class Line:
    def __init__(self, gui, start, end, borderWidth, borderCol):
        self.gui = gui
        self.start, self.end = start, end
        self.width = borderWidth
        self.colour = borderCol

    def Draw(self):
        line(self.gui.display, self.colour, (self.start[0]*self.gui.size[0], self.start[1]*self.gui.size[1]),
             (self.end[0]*self.gui.size[0], self.end[1]*self.gui.size[1]), self.width)
