#! python3
# __main__.py - test all modules through pygame

import os, sys
import pygame
import WordToPdf, MathTools, EnglishTools

def main():
    """the main function to show all the functions via pygame"""

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    while True:
        screen.fill((0,0,50))
        pygame.display.update()


print(0)