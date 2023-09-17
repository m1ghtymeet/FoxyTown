import pygame as pg
from Data.utils.Settings import *

tile_rects = []

gem_group = pg.sprite.Group()

class Tilemap:
    def __init__(self, maps, images):
        self.maps = maps
        self.images = images

    def change_map(self, maps):
        self.maps = maps

    def draw(self, surf, scroll):
        y = 0
        for row in self.maps:
            x = 0
            for tile in row:
                if tile == "1":
                    surf.blit(self.images["Grass-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                    if debug:
                        pg.draw.rect(surf, (255, 0, 0), pg.Rect(x * 48 - scroll[0], y * 48 - scroll[1], 48, 48), 1)
                if tile == "2":
                    surf.blit(self.images["Grass-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                    if debug:
                        pg.draw.rect(surf, (255, 0, 0), pg.Rect(x * 48 - scroll[0], y * 48 - scroll[1], 48, 48), 1)
                if tile == "3":
                    surf.blit(self.images["Grass-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "4":
                    surf.blit(self.images["Dirt-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "5":
                    surf.blit(self.images["Dirt-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "6":
                    surf.blit(self.images["Dirt-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                    if debug:
                        pg.draw.rect(surf, (255, 0, 0), pg.Rect(x * 48 - scroll[0], y * 48 - scroll[1], 48, 48), 1)
                if tile == "7":
                    surf.blit(self.images["Grass-air-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "8":
                    surf.blit(self.images["Grass-air-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "9":
                    surf.blit(self.images["Grass-air-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "a":
                    surf.blit(self.images["Stone-ancient-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "b":
                    surf.blit(self.images["Stone-ancient-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "c":
                    surf.blit(self.images["Stone-ancient-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "d":
                    surf.blit(self.images["Stone-brick"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "e":
                    surf.blit(self.images["Stone-brick-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "f":
                    surf.blit(self.images["Rock-brick"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "g":
                    surf.blit(self.images["Rock-big"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "h":
                    surf.blit(self.images["Rock-small"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "i":
                    surf.blit(self.images["Stone-ancient-center-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "j":
                    surf.blit(self.images["Stone-brick-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "k":
                    surf.blit(self.images["Stone-ancient-center-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "l":
                    surf.blit(self.images["Stone-ancient-down-left"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "m":
                    surf.blit(self.images["Stone-ancient-down-middle"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "n":
                    surf.blit(self.images["Stone-ancient-down-right"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "o":
                    surf.blit(self.images["Stone-brick"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "p":
                    surf.blit(self.images["Grass-one"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile == "q":
                    surf.blit(self.images["Grass-two"], (x * 48 - scroll[0], y * 48 - scroll[1]))
                if tile != "0" and tile != "j" and tile != "o" and tile != "p" and tile != "q":
                    tile_rects.append(pg.Rect(x * 48, y * 48, 48, 48))
                x += 1
            y += 1