import pygame as pg

class Spritesheet:
    def __init__(self, image):
        self.sheet = image
        self.orig = (-3, -8)

    def get_image(self, frame, width, height, scale=1):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, self.orig, ((frame * width), 0, width, height))
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))

        return image

    def change_image(self, image):
        self.sheet = image

    def set_colorkey(self, color):
        self.sheet.set_colorkey(color)

    def set_origin(self, orig):
        self.orig = orig