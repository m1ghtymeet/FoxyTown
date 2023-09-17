import pygame as pg
from Data.utils.Spritesheet import *
from Data.utils.Settings import *

class Player:
    def __init__(self, pos, images):
        self.sprite = Spritesheet(images["Idle"])
        self.sprite_num = 0
        self.image = self.sprite.get_image(self.sprite_num, 33, 32, 2.7)
        self.rect = pg.Rect(pos[0], pos[1], 33 * 2, 32 * 2)

        self.movement = [False, False]
        self.velocity = 0
        self.flip = False
        self.direction = 1
        self.speed = 5
        self.air_count = 0
        self.in_air = False
        self.damaged = False

        self.sprite_count = 0
        self.action = "Idle"

        self.alive = True
        self.health = 100
        self.gems = 0

    def update(self, images, tile_r, scroll):

        # scroll[0] += (self.rect.x-scroll[0]-960)/5
        # scroll[1] += (self.rect.y-scroll[1]-540)/5
        scroll[0] += (self.rect.x-scroll[0]-350)/5
        scroll[1] += (self.rect.y-scroll[1]-250)/5

        movements = [0, 0]

        if self.alive:
            self.move(movements)
        else:
            self.action = "Hurt"

        self.animation(images)
        self.check(tile_r, movements)
        self.check_alive()

        if self.alive == False:
            scroll[1] -= 5
            if scroll[1] <= -50:
                scroll[1] = -50

    def move(self, movements):
        if self.movement[0]:
            movements[0] -= self.speed
            self.flip = True
            self.action = "Run"
        elif self.movement[1]:
            movements[0] += self.speed
            self.flip = False
            self.action = "Run"
        else:
            self.action = "Idle"

    def animation(self, images):

        if self.velocity <= -1:
            self.action = "Jump"
        if self.velocity >= .8:
            self.action = "Fall"

        if self.damaged:
            self.action = "Hurt"

        self.sprite_count += 1
        if self.sprite_count >= 5:
            self.sprite_num += 1

            if self.action == "Idle":
                if self.sprite_num >= 4:
                    self.sprite_num = 0
            if self.action == "Run":
                if self.sprite_num >= 6:
                    self.sprite_num = 0
            if self.action == "Jump":
                if self.sprite_num >= 0:
                    self.sprite_num = 0
            if self.action == "Fall":
                if self.sprite_num >= 0:
                    self.sprite_num = 1
            if self.action == "Hurt":
                if self.sprite_num >= 2:
                    self.sprite_num = 0

            self.sprite_count = 0

        self.image = self.sprite.get_image(self.sprite_num, 33, 32, 2.7)

        if self.action == "Idle":
            self.sprite.change_image(images["Idle"])
        if self.action == "Run":
            self.sprite.change_image(images["Run"])
        if self.action == "Jump":
            self.sprite.change_image(images["Jump"])
        if self.action == "Fall":
            self.sprite.change_image(images["Jump"])
        if self.action == "Hurt":
            self.sprite.change_image(images["Hurt"])

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.speed = 0

    def check(self, tile_r, movements):
        movements[1] += self.velocity
        self.velocity += .2
        if self.velocity >= 10:
            self.velocity = 10

        self.rect, collision = moving(self.rect, tile_r, movements)

        if collision['bottom']:
            self.velocity = 0
            self.air_count = 0
        else:
            self.air_count += 1

        if collision['top']:
            self.velocity = 0

        if self.health > 100:
            self.health = 100

    def inputs(self, e):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_a:
                self.movement[0] = True
            if e.key == pg.K_d:
                self.movement[1] = True
            if e.key == pg.K_SPACE:
                if self.air_count <  6:
                    self.velocity = -7

        if e.type == pg.KEYUP:
            if e.key == pg.K_a:
                self.movement[0] = False
            if e.key == pg.K_d:
                self.movement[1] = False

    def draw(self, surf, scroll):
        self.image = pg.transform.flip(self.image, self.flip, False)
        self.image.set_colorkey((0, 0, 0))
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))
        # pg.draw.rect(surf, (255, 0, 0), self.rect, 1)
