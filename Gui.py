import pygame

class Gui:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.width = width
        self.height = height
        self.size = (1, 1)
        self.monitorSize = pygame.display.Info().current_w, pygame.display.Info().current_h
        if width > self.monitorSize[0]:
            self.reAdjust(self.monitorSize[0], height)
        if height > self.monitorSize[1]:
            self.reAdjust(width*self.size[0], self.monitorSize[1])

    def reAdjust(self, width, height):
        self.size = (width/self.width, height/self.height)

    def Load(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.VIDEORESIZE:
                self.reAdjust(event.w, event.h)