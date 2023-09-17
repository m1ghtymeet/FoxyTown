import pygame as pg
from Data.utils.Spritesheet import *

class Gem(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.sprite = Spritesheet(pg.image.load("Image/spritesheets/gem.png").convert_alpha())
        self.frame_index = 0
        self.image = self.sprite.get_image(self.frame_index, 15, 13, 2.7)
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

        self.frame_count = 0

    def update(self, player):

        self.animation()

        if player.rect.colliderect(self.rect):
            player.gems += 1
            self.kill()

    def animation(self):
        
        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame_index += 1
            if self.frame_index >= 5:
                self.frame_index = 0
            self.frame_count = 0

        self.image = self.sprite.get_image(self.frame_index, 15, 13, 2.7)

    def draw(self, surf, scroll):
        self.sprite.set_origin((0, 0))
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))

class Cherry(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.sprite = Spritesheet(pg.image.load("Image/spritesheets/cherry.png").convert_alpha())
        self.frame_index = 0
        self.image = self.sprite.get_image(self.frame_index, 21, 21, 2.7)
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

        self.frame_count = 0

    def update(self, player):

        self.animation()

        if player.rect.colliderect(self.rect):
            if player.health <= 100:
                player.health += 20
                self.kill()

    def animation(self):
        
        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame_index += 1
            if self.frame_index >= 5:
                self.frame_index = 0
            self.frame_count = 0

        self.image = self.sprite.get_image(self.frame_index, 21, 21, 2.7)

    def draw(self, surf, scroll):
        self.sprite.set_origin((0, 0))
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))