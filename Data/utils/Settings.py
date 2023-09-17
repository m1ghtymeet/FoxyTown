import pygame as pg

debug = False

images = {
    "Idle": pg.image.load("Image/spritesheets/player-idle.png"),
    "Run": pg.image.load("Image/spritesheets/player-run.png"),
    "Jump": pg.image.load("Image/spritesheets/player-jump.png"),
    "Hurt": pg.image.load("Image/spritesheets/player-hurt.png")
}
images_tile = {
    "Grass-left": pg.transform.scale(pg.image.load("Image/environment/grass-left.png"), (48, 48)),
    "Grass-middle": pg.transform.scale(pg.image.load("Image/environment/grass-middle.png"), (48, 48)),
    "Grass-right": pg.transform.scale(pg.image.load("Image/environment/grass-right.png"), (48, 48)),
    "Grass-air-left": pg.transform.scale(pg.image.load("Image/environment/grass-air-left.png"), (48, 48)),
    "Grass-air-middle": pg.transform.scale(pg.image.load("Image/environment/grass-air-middle.png"), (48, 48)),
    "Grass-air-right": pg.transform.scale(pg.image.load("Image/environment/grass-air-right.png"), (48, 48)),
    "Dirt-left": pg.transform.scale(pg.image.load("Image/environment/dirt-left.png"), (48, 48)),
    "Dirt-middle": pg.transform.scale(pg.image.load("Image/environment/dirt-middle.png"), (48, 48)),
    "Dirt-right": pg.transform.scale(pg.image.load("Image/environment/dirt-right.png"), (48, 48)),
    "Dirt-right": pg.transform.scale(pg.image.load("Image/environment/dirt-right.png"), (48, 48)),
    "Stone-ancient-left": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-left.png"), (48, 48)),
    "Stone-ancient-middle": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-middle.png"), (48, 48)),
    "Stone-ancient-right": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-right.png"), (48, 48)),
    "Stone-brick": pg.transform.scale(pg.image.load("Image/environment/stone-brick.png"), (48, 48)),
    "Stone-brick-middle": pg.transform.scale(pg.image.load("Image/environment/stone-brick-middle.png"), (48, 48)),
    "Rock-brick": pg.transform.scale(pg.image.load("Image/environment/rock-brick.png"), (48, 48)),
    "Rock-big": pg.transform.scale(pg.image.load("Image/environment/rock-big.png"), (48, 48)),
    "Rock-small": pg.transform.scale(pg.image.load("Image/environment/rock-small.png"), (48, 48)),
    "Stone-ancient-center-left": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-center-left.png"), (48, 48)),
    "Stone-ancient-center-right": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-center-right.png"), (48, 48)),
    "Stone-ancient-down-left": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-down-left.png"), (48, 48)),
    "Stone-ancient-down-middle": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-down-middle.png"), (48, 48)),
    "Stone-ancient-down-right": pg.transform.scale(pg.image.load("Image/environment/stone-ancient-down-right.png"), (48, 48)),
    "Grass-one": pg.transform.scale(pg.image.load("Image/environment/grass-one.png"), (48, 48)),
    "Grass-two": pg.transform.scale(pg.image.load("Image/environment/grass-two.png"), (48, 48)),
}



def load_map(path):
    f = open(f"{path}.txt", "r")
    data = f.read()
    f.close()
    data = data.split("\n")
    maps = []
    for row in data:
        maps.append(list(row))
    return maps

def collision_check(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def moving(rect, tiles, movement):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_check(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["right"] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    rect.y += movement[1]
    hit_list = collision_check(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

class HealthBar:
    def __init__(self, pos, health):
        self.x = pos[0]
        self.y = pos[1]
        self.health = health

    def draw(self, surf, health):
        self.health = health

        ratio = self.health / 100
        pg.draw.rect(surf, (0, 0, 0), (self.x - 2, self.y - 2, 154, 24))
        pg.draw.rect(surf, (255, 0, 0), (self.x, self.y, 150, 20))
        pg.draw.rect(surf, (0, 255, 0), (self.x, self.y, 150 * ratio, 20))

class ScreenFade:
    def __init__(self, direction, color, speed):
        self.direction = direction
        self.color = color
        self.speed = speed
        self.fade_count = 0

    def fade(self, surf):
        fade_complate = False
        self.fade_count += self.speed
        if self.direction == 1:
            pg.draw.rect(surf, self.color, (0 - self.fade_count, 0, 800 // 2, 600))
            pg.draw.rect(surf, self.color, (800 // 2 + self.fade_count, 0, 800, 600))
            pg.draw.rect(surf, self.color, (0, 0 - self.fade_count, 800, 600 // 2))
            pg.draw.rect(surf, self.color, (0, 600 // 2 + self.fade_count, 800, 600))
        if self.direction == 2:
            pg.draw.rect(surf, self.color, (0, 0, 800, 0 + self.fade_count))
        if self.fade_count >= 800:
            fade_complate = True
        return fade_complate
