import pygame
from banana import Banana
import home
import cv2 as cv
import run
import random
import cam

def main_window(background):
    pygame.init()
    font = pygame.font.Font(None, 40)
    banana_drop = 50
    pygame.time.set_timer(banana_drop, 3000)
    high_score = 500
    score = 0
    mili_second = 60 
    second = 4
    game_over = False
    all_banana_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    Banana.containers = all_sprites, all_banana_list
    
    home.home_window(background)
    cap = cv.VideoCapture(0)
    cap.set(3, run.width)
    cap.set(4, run.height)

    while True:
        for event in pygame.event.get():
            if event.dict.get('key') == 27:
                game_over = True
            elif event.type == banana_drop:
                for i in range(random.randint(2, 5)):
                    Banana('Asset/banana.png', random.randint(0, run.width-20), -5, random.randint(2, 10))
            elif score == high_score:
                game_over = True
            
        frame, position = cam.get_frame(cap)

        if game_over != True:
            mili_second -= 1
        if mili_second == 0:
            if second != 0:
                second -= 1
            elif second == 0:
                game_over = True
            if game_over != True:
                mili_second = 59

        run.screen.blit(frame, (0, 0))
        score_text = font.render(f'Score: {score}', True, (0, 255, 255), None)
        run.screen.blit(score_text, (5, 5))
        timer_text = font.render(f'Timer: {second}.{mili_second} s', True, (57, 255, 20), None)
        run.screen.blit(timer_text, (750, 5))

        if not game_over:
            for banana in all_banana_list:
                score = banana.update(score, position)
            for banana in all_banana_list:
                all_banana_list.remove(banana)
                banana.collide(all_banana_list)
                all_banana_list.add(banana)
        else:
            font1 = pygame.font.Font(None, 50)
            result = font1.render(f'Your Score : {score}', True, (255, 255, 0), None)
            run.screen.blit(result, ((run.width/2)-125, run.height/2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.quit()

        pygame.display.flip()
        run.clock.tick(60)
            