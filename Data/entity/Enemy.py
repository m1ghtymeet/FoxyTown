from this import d
import pygame as pg
from Data.utils.Spritesheet import *
from Data.utils.Settings import *
import random

class Oposum(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.sprite = Spritesheet(pg.image.load("Image/spritesheets/oposum.png").convert_alpha())
        self.frame_index = 0
        self.image = self.sprite.get_image(self.frame_index, 36, 28, 1.5)
        self.rect = self.image.get_rect()
        self.rect.height = 40
        self.rect.center = (pos[0], pos[1])

        self.movement = [False, False]
        self.velocity = 0
        self.flip = False
        self.direction = 1
        self.frame_count = 0
        self.move_count = 0
        self.damage_cooldown = 0
        self.speed = 2

    def update(self, tile_r, player):
        self.animation()

        movements = [0, 0]

        movements[1] += self.velocity
        self.velocity += .2

        self.rect, collision = moving(self.rect, tile_r, movements)
        if collision['bottom']:
            self.velocity = 0

        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1

        if player.rect.colliderect(self.rect):
            if self.damage_cooldown == 0:
                self.damage_cooldown = 20
                player.health -= 15
                player.velocity = -5
                player.damaged = True
        else:
            player.damaged = False

    def ai(self, player):
        if self.direction == 1:
            self.movement[1] = True
        else:
            self.movement[1] = False
        self.movement[0] = not self.movement[1]
        self.move()
        self.move_count += 1

        if self.move_count > 48:
            self.direction *= -1
            self.move_count *= -1

    def move(self):
        if self.movement[0]:
            self.rect.x -= self.speed
            self.flip = False
            self.direction = -1
        if self.movement[1]:
            self.rect.x += self.speed
            self.flip = True
            self.direction = 1

    def animation(self):

        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame_index += 1
            if self.frame_index >= 6:
                self.frame_index = 0
            self.frame_count = 0

        self.image = self.sprite.get_image(self.frame_index, 36, 28, 2)

    def draw(self, surf, scroll):
        self.image = pg.transform.flip(self.image, self.flip, False)
        self.image.set_colorkey((0, 0, 0))
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))

class Eagle(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.sprite = Spritesheet(pg.image.load("Image/spritesheets/eagle-attack.png").convert_alpha())
        self.frame_index = 0
        self.image = self.sprite.get_image(self.frame_index, 40, 41, 1.5)
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

        self.movement = [0, 0]
        self.direction = 1
        self.flip = False
        self.frame_count = 0
        self.move_count = 0
        self.damage_cooldown = 0
        self.speed = 2

    def update(self, player):
        self.animation()

        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1

        if self.rect.colliderect(player.rect):
            if self.damage_cooldown == 0:
                self.damage_cooldown = 20
                player.health -= 30

    def ai(self, player):
        if self.direction == 1:
            self.movement[1] = True
        else:
            self.movement[1] = False
        self.movement[0] = not self.movement[1]
        self.move()
        self.move_count += 1

        if self.move_count > 48:
            self.direction *= -1
            self.move_count *= -1

    def move(self):
        if self.movement[0]:
            self.rect.x -= self.speed
            self.flip = False
            self.direction = -1
        if self.movement[1]:
            self.rect.x += self.speed
            self.flip = True
            self.direction = 1

    def animation(self):

        self.frame_count += 1
        if self.frame_count >= 5:
            self.frame_index += 1
            if self.frame_index >= 4:
                self.frame_index = 0
            self.frame_count = 0

        self.image = self.sprite.get_image(self.frame_index, 40, 41, 1.5)

    def draw(self, surf, scroll):
        self.image = pg.transform.flip(self.image, self.flip, False)
        self.image.set_colorkey((0, 0, 0))
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))