import pygame as pg
from Data.entity.Player import *
from Data.entity.Enemy import *
from Data.tile.Tilemap import *
from Data.tile.Item import *
from Data.ui.Button import *
from Data.tile.Door import *

width = 800
height = 600

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Sunny Land | Demo ')
clock = pg.time.Clock()
pg.mouse.set_visible(False)

#  door_open_fx = pg.mixer.Sound('Audio/DoorOpen.wav')
# door_open_fx.set_volume(2)

mouse_image = pg.image.load("Image/Graphics/mouse.png")

# Groups
oposum_group = pg.sprite.Group()
eagle_group = pg.sprite.Group()
gem_group = pg.sprite.Group()
cherry_group = pg.sprite.Group()
door_group = pg.sprite.Group()

player = Player([100, 100], images)

# Enemy
ops = Oposum([2400, 100])
ops2 = Oposum([2600, 100])
ops3 = Oposum([900, 100])
eagle = Eagle([2400, 100])

healthBar = HealthBar([10, 10], player.health)

door = Door([349, 240])
door2 = Door([2650, 288])

gem = Gem([2200, 100])
gem2 = Gem([2500, 200])
gem3 = Gem([2500, 300])
gem4 = Gem([2500, 250])
gem5 = Gem([2600, 200])
gem6 = Gem([2700, 250])

cher = Cherry([100, 200])
cher2 = Cherry([1000, 100])

# Add
oposum_group.add(ops)
oposum_group.add(ops2)
oposum_group.add(ops3)

eagle_group.add(eagle)

gem_group.add(gem)
gem_group.add(gem2)
gem_group.add(gem3)
gem_group.add(gem4)
gem_group.add(gem5)
gem_group.add(gem6)

cherry_group.add(cher)

def draw_text(font, text, pos, color=(255, 255, 255)):
    image = font.render(text, True, color, (0, 0, 0))
    image.set_colorkey((0, 0, 0))
    screen.blit(image, (pos[0] - (image.get_width() / 2), pos[1]))
