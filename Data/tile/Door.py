import pygame as pg

class Door(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/environment/props/door.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.opened = False
        self.action = False

    def update(self, player, level_complate):
        if self.opened == False:
            self.image = pg.transform.scale(pg.image.load("Image/environment/props/door.png").convert_alpha(), (44, 66))
        else:
            self.image = pg.transform.scale(pg.image.load("Image/environment/props/door-opened.png").convert_alpha(), (44, 66))

        if self.opened:
            if self.rect.colliderect(player.rect):
                self.action = True
                level_complate = True
            else:
                self.action = False

    def draw(self, surf, scroll):
        surf.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))