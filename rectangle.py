import pygame
import random

class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.selected = False
        self.correct_position = 0

    def draw(self, gameDisplay, position):

        if self.selected: # If the rectangle is selected
            color = (200, 0 ,0)
            self.selected = False
        elif self.selected == None: # If the right rectangle is found
            color = (0, 0, 200)
            self.selected = False
        else:
            color = self.color
            
        pygame.draw.rect(gameDisplay, color, (self.display_width / self.amount * position, self.display_height - self.height, self.width, self.height))

    def select(self, found=False):
        self.selected = True
        if found:
            self.selected = None

    # --------  static functions  --------

    @staticmethod
    def set_dimentions(display_width, display_height, sorter_box_height):
        rectangle.display_width = display_width
        rectangle.display_height = display_height
        rectangle.sorter_box_height = sorter_box_height

    
    @staticmethod
    def generate_rectangles(amount): # Generates rectangles with the correct width and height, so that the canvas is filled out
        rectangle.amount = amount
        rectangels = []

        for i in range(amount):
            width = round(rectangle.display_width / amount + 0.5)
            height = int(rectangle.sorter_box_height / amount * (i + 1) + 0.5)
            
            rectangels.append(rectangle(width, height))
        
        rectangels = rectangle.set_color(rectangels, (200, 0, 0))

        return rectangels

    @staticmethod
    def set_color(rectangles, new_color):# Gives the colors the fade
        for i in range(0, len(rectangles)):
            rectangles[i].color = (new_color[0] / rectangle.amount * rectangles[i].correct_position, (new_color[1] / rectangle.amount * rectangles[i].correct_position), new_color[2] / rectangle.amount * rectangles[i].correct_position)
        return rectangles

    @staticmethod
    def shuffle(rectangles):
        for i in range(0, len(rectangles)):
            rectangles[i].correct_position = i
        random.shuffle(rectangles)