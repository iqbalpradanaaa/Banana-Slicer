import pygame
import run

pygame.display.set_caption("Banana Slicer Game")
background = pygame.image.load("Asset/bg.png").convert_alpha()
background = pygame.transform.scale(background, (run.width, run.height))

def home_window(background):
    pygame.init()
    font = pygame.font.Font(None, 40)
    running = True
    while running:
        for event in pygame.event.get():
            if event.dict.get('key') == 27:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
        run.screen.blit(background, (0,0))
        start_text = font.render("Enter Any Key to Start Game", True, (69, 67, 153), None)
        run.screen.blit(start_text, (100, 210))
        pygame.display.flip()