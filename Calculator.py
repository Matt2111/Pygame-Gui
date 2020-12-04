import pygamegui
import pygame

class Calculator(pygamegui.Gui):
    def __init__(self):
        super().__init__(500, 600)
        self.answer = "0"
        self.current = None
        self.previous = None
        self.operator = None
        self.displayScreen = pygamegui.Rectangle(self, (0, 0), (500, 100), 8, (50, 50, 50), (10, 100, 10))

        # Numbers buttons
        self.numberButtons = list()
        for x in range(3):
            for y in range(3):
                button = pygamegui.Button(self, (x*125, y*125+100), (125, 125), 3, (50, 50, 50), (75, 75, 75))
                button.AttachText(str((9-y*3)-(2-x)), "Arial Rounded", 30, (255, 255, 255))
                button.SetLeft(self.ChangeCurrent, [str((9-y*3)-(2-x))])
                self.numberButtons.append(button)
        button = pygamegui.Button(self, (125, 475), (125, 125), 3, (50, 50, 50), (75, 75, 75))
        button.AttachText("0", "Arial Rounded", 30, (255, 255, 255))
        button.SetLeft(self.ChangeCurrent, ["0"])
        self.numberButtons.append(button)
        button = pygamegui.Button(self, (0, 475), (125, 125), 3, (50, 50, 50), (75, 75, 75))
        button.AttachText("C", "Arial Rounded", 30, (255, 255, 255))
        button.SetLeft(self.Clear, None)
        self.numberButtons.append(button)

        # Operator buttons
        self.operatorButtons = list()
        operators = ["+", "-", "×", "÷"]
        for y in range(4):
            button = pygamegui.Button(self, (375, y*125+100), (125, 125), 3, (50, 50, 50), (75, 75, 75))
            button.AttachText(operators[y], "Arial Rounded", 30, (255, 255, 255))
            button.SetLeft(self.ChangeOperator, args=[operators[y]])
            self.operatorButtons.append(button)
        button = pygamegui.Button(self, (250, 475), (125, 125), 3, (50, 50, 50), (75, 75, 75))
        button.AttachText("=", "Arial Rounded", 30, (255, 255, 255))
        button.SetLeft(self.ShowAnswer, None)
        self.operatorButtons.append(button)
        self.Run()

    def Clear(self):
        self.previous = None
        self.operator = None
        self.current = None
        self.answer = "0.0"

    def Solve(self, operator):
        if self.current is not None:
            if operator == "+":
                self.answer = float(self.current) + self.previous
                self.previous = self.answer
                self.current = None
            elif operator == "-":
                self.answer = self.previous - float(self.current)
                self.previous = self.answer
                self.current = None
            elif operator == "×":
                self.answer = self.previous * float(self.current)
                self.previous = self.answer
                self.current = None
            elif operator == "÷":
                self.answer = self.previous / float(self.current)
                self.previous = self.answer
                self.current = None
            self.answer *= 100
            self.answer = float(str(self.answer).split(".")[0])/100

    def ShowAnswer(self):
        self.Solve(self.operator)

    def ChangeOperator(self, operator):
        if self.current is not None:
            self.previous = float(self.current)
            self.current = None
            self.operator = operator
        else:
            self.operator = operator

    def ChangeCurrent(self, num):
        if self.current is None:
            self.current = str()
        if len(self.current) < 9:
            self.current += num

    def Run(self):
        while True:
            self.display.fill((0, 0, 0))
            self.Load()

            if self.current is None:
                self.displayScreen.AttachText(str(self.answer), "Arial Rounded", 40, (255, 255, 255), pos=(2, 1))
            else:
                self.displayScreen.AttachText(self.current, "Arial Rounded", 40, (255, 255, 255), pos=(2, 1))
            self.displayScreen.Draw()

            for button in self.numberButtons:
                button.Draw()
                button.Clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3))
            for button in self.operatorButtons:
                button.Draw()
                button.Clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3))

            pygame.display.update()

calculator = Calculator()
