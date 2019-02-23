import random
import pygame

import sorter
import Rectangle

# Gets the settings from "settings.txt"
settings = [line.split(": ")[1] for line in open("settings.txt", "r").read().split("\n")[:5]]
amount = int(settings[0])
speed = settings[1]
repeat = settings[2]
display_width = int(settings[3])
display_height = int(settings[4])
sorter_box_height = display_height - 100

color = (0, 200, 0)

pygame.init()
pygame.font.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Rectangle Sorter")
clock = pygame.time.Clock()


def main_loop():
    Rectangle.rectangle.set_dimentions(display_width, display_height, sorter_box_height)
    rectangles = Rectangle.rectangle.generate_rectangles(amount)
    Rectangle.rectangle.shuffle(rectangles)
    rectangles = Rectangle.rectangle.set_color(rectangles, color)

    # Buttons
    start = button(25, 25, 100, 50, "START", (100, 100, 100), (110, 110, 110))
    stop = button(150, 25, 100, 50, "STOP", (100, 100, 100), (110, 110, 110))
    reset = button(275, 25, 100, 50, "RESET", (75, 75, 75), (85, 85, 85))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((255, 255, 255))
        
        # Button drawing
        start.draw(gameDisplay)
        stop.draw(gameDisplay)
        reset.draw(gameDisplay)

        # Colors
        tmp_color = color
        draw_colorboxes(gameDisplay)
        if tmp_color != color:
            rectangles = Rectangle.rectangle.set_color(rectangles, color)

        if button.on:
            rectangles = sorter.sort(rectangles, repeat)# Sorting

        if button.reset or sorter.done and repeat == "on":# Reseting
            rectangles = Rectangle.rectangle.generate_rectangles(amount)
            Rectangle.rectangle.shuffle(rectangles)
            rectangles = Rectangle.rectangle.set_color(rectangles, color)
            button.reset = False
            sorter.reset()

        draw_rectangles(rectangles)

        pygame.display.update()

        if speed.isdigit():
            clock.tick(int(speed))


class button:# The start, stop and reset buttons
    on = False
    reset = False
    resetable = False

    def __init__(self, x, y, width, height, text, color, second_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.second_color = second_color


    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, (self.x, self.y, self.width, self.height))

        self.click_listening()

        font = pygame.font.SysFont('Consolas', 30, bold=True)
        font = font.render(self.text, True, (0, 0, 0))
        gameDisplay.blit(font,(self.x + (self.width / 2) - (font.get_width() / 2), self.y + 10))
    
    def click_listening(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > self.x and mouse[0] < self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:# If it's clicked
            pygame.draw.rect(gameDisplay, self.second_color, (self.x, self.y, self.width, self.height))
            if click[0]:
                if self.text == "START":
                    button.on = True
                if self.text == "STOP":
                    button.on = False
                if self.text == "RESET":
                    if button.resetable:# Makes sure it's not reset multiple times, if the mouse is held down
                        button.reset = True
                    button.resetable = False
            else:
                button.resetable = True
        


def draw_colorboxes(gameDisplay):
    global color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    font = pygame.font.SysFont('Consolas', 25, bold=True)
    font = font.render("Colors", True, (0, 0, 0))
    gameDisplay.blit(font,(415, 37))

    x = 510
    y = 37
    spaceing = 10
    width = 25
    colors = [(200, 0, 0), (0, 200, 0), (30, 30, 255), (200, 200, 0), (200, 0, 200), (0, 200, 200), (0, 0, 0)]
    for i in range(0, len(colors)):
        if mouse[0] > x + (i * spaceing) + (i * width) and mouse[0] < x + (i * spaceing) + (i * width) + width and mouse[1] > y and mouse[1] < y + width:# If it's clicked
            if click[0]:
                color = colors[i]
        pygame.draw.rect(gameDisplay, colors[i], (x + (i * spaceing) + (i * width), y, width, width))



def draw_rectangles(rectangles):
    for i in range(0, len(rectangles)):
        rectangles[i].draw(gameDisplay, i)



main_loop()