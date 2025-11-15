import pygame
from pygame import mixer
import home
import main

width, height = 960, 540
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

if __name__ == '__main__':
    mixer.init()
    mixer.music.load("Asset/dazai.mp3")
    mixer.music.play(-1)
    main.main_window(home.background)