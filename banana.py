import pygame
import run

class Banana(pygame.sprite.Sprite):
    def __init__(self, banana_img, x, y, speed):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(banana_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.radius = 25
    
    def update(self, score, position):
        run.screen.blit(self.image, (self.rect))
        # print (position)
        if self.rect.y >= run.height:
            score -= 1
            self.kill()
        elif self.rect.y >= 0 or self.rect.y <= 0:
            self.rect.y += self.speed
            if self.rect.collidepoint(*position):
                pop = pygame.image.load("Asset/splash.png").convert_alpha()
                pop = pygame.transform.scale(pop, (120, 120))
                self.image = pop
                run.screen.blit(pop, (self.rect.x, self.rect.y))
                score += 1
                self.kill()
        return score
    
    def collide(self, all_banana_list):
        collections = pygame.sprite.spritecollide(self, all_banana_list, False, pygame.sprite.collide_circle)
        for each in collections:
            if each.speed == 0:
                self.speed = 0