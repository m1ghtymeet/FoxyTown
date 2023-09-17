import pygame as pg
from pygame.locals import *
from pygame import mixer
from Data.utils.const import *
import json

pg.init()

# variables
text = ['']
font_size = 60
level = 1
MAX_LEVELS = 3
level_compalte = False
game_state = "etname"
scroll = [0, 0]
death_count = 0
stayCount = 0

# Tilemap
levels = load_map(f"level/level0{level}")
tilemap = Tilemap(levels, images_tile)

font = pg.font.Font("Font/F.ttf", 25)
erfanFont = pg.font.Font("Font/Erfan.ttf", font_size)

# Buttons
submit_button = Button([330, 400], "Submit", (255, 165, 0), (196, 95, 0), (0, 0, 0))
start_button = Button([320, 200], "Play", (255, 255, 0), (196, 196, 0), (0, 0, 0))
exit_button = Button([320, 330], "Exit", (255, 0, 0), (196, 0, 0), (0, 0, 0))
congrulotion_button = Button([width / 2, 350], "Exit", (255, 180, 0), (190, 90, 0), (0, 0, 0))

# Screen Fade 
play_fade = ScreenFade(1, (0, 0, 0), 4)
death_fade = ScreenFade(2, (255, 196, 196), 4)
congrulotion_fade = ScreenFade(2, (0, 0, 0), 4)

run = True
while run:
    if game_state == "etname":
        screen.fill((0, 0, 0))
    if game_state == "menu":
        screen.fill((255, 255, 255))
    if game_state == "game":
        screen.fill((71, 243, 255))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
                
        if game_state == "etname":
            if e.type == pg.TEXTINPUT:
                text[-1] += e.text
                
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_BACKSPACE:
                    text[-1] = text[-1][:-1]
                    if len(text[-1]) == 0:
                        if len(text) > 1:
                            text = text[:-1]
                
        if game_state == "game":
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_t:
                    if debug == False:
                        debug = True
                if e.key == pg.K_w:
                    for doors in door_group:
                        if doors.rect.colliderect(player.rect):
                            if doors.action:
                                level += 1
                                if level == 3:
                                    player.rect.x = 100
            player.inputs(e)

    # Enter Name
    if game_state == "etname":
        draw_text(erfanFont, "Enter Your Name:", [800 / 2, 100])
    
        for row, line in enumerate(text):
            draw_text(erfanFont, line, [800 / 2, 200 + (row * font_size)])
        
        if text[-1] != "":
            if submit_button.draw(screen):
                data_file = open("data.txt", "w")
                data_file.write(text[-1])
                data_file.close()
                game_state = "menu"
        
        pos = pg.mouse.get_pos()
        screen.blit(pg.transform.scale(mouse_image, (14, 24)), pos)
        
    # Menu
    if game_state == "menu":
        erfanFont = pg.font.Font("Font/Erfan.ttf", 100)
        draw_text(erfanFont, "Foxy Town", [width/2, 10], (0, 0, 0))

        erfanFont = pg.font.Font("Font/Erfan.ttf", 50)
        draw_text(erfanFont, "Demo", [width/2-100, 90], (0, 0, 0))
        draw_text(erfanFont, f"Name: {text[-1]}", [width/2, 400], (0, 0, 0))

        if start_button.draw(screen):
            game_state = "game"
        if exit_button.draw(screen):
            run = False
            exit()

        pos = pg.mouse.get_pos()
        screen.blit(pg.transform.scale(mouse_image, (14, 24)), pos)

    # Game
    if game_state == "game":

        # print(f"x: {player.rect.x - scroll[0]}, y: {player.rect.y - scroll[1]}")

        for doors in door_group:
            if player.gems > 5:
                door.opened = True
            else:
                draw_text(font, "You Need Gem For Open Door", [doors.rect.centerx - scroll[0], doors.rect.centery - 100 - scroll[1]], (0,0,0))

        if level == 1:

            door_group.add(door)

            for doors in door_group:
                doors.update(player, level_compalte)
                doors.draw(screen, scroll)

                if doors.rect.colliderect(player.rect):
                    if doors.opened:
                        draw_text(erfanFont, "W", [player.rect.centerx + 10 - scroll[0], player.rect.centery - 85 - scroll[1]], (0, 0, 0))

            for op in oposum_group:
                op.ai(player)
                op.update(tile_rects, player)
                op.draw(screen, scroll)

            for eagles in eagle_group:
                eagles.ai(player)
                eagles.update(player)
                eagles.draw(screen, scroll)

            for gems in gem_group:
                gems.update(player)
                gems.draw(screen, scroll)

            for chers in cherry_group:
                chers.update(player)
                chers.draw(screen, scroll)

            tilemap.draw(screen, scroll)

            player.update(images, tile_rects, scroll)
            player.draw(screen, scroll)

        if level == 2:

            if player.gems > 5:
                door.opened = True
            else:
                draw_text(erfanFont, "You Need Gem For Open Door", [door2.rect.x - 100 - scroll[0], door2.rect.y - 100 - scroll[1]], (0,0,0))

            tile_rects.clear()

            levels = load_map(f"level/level0{level}")

            cherry_group.add(cher2)

            door_group.remove(door)
            door_group.add(door2)

            for chers in cherry_group:
                chers.update(player)
                chers.draw(screen, scroll)

            for doors in door_group:
                doors.update(player, level_compalte)
                doors.draw(screen, scroll)
                doors.opened = True

                if doors.rect.colliderect(player.rect):
                    if doors.opened:
                        draw_text(erfanFont, "W", [player.rect.centerx + 10 - scroll[0], player.rect.centery - 85 - scroll[1]], (0, 0, 0))

            tilemap.change_map(levels)
            tilemap.draw(screen, scroll)

            player.update(images, tile_rects, scroll)
            player.draw(screen, scroll)

        if level == 3:
        
            stayCount += 1
            
            if stayCount >= 800:
                screen.fill((0, 0, 0))
            else:
                font_size = 100
                erfanFont = pg.font.Font("Font/Erfan.ttf", font_size)
                draw_text(erfanFont, "Congratulations!", [500 - scroll[0], 50 - scroll[1]], (0, 0, 0))
                draw_text(erfanFont, "Thank You For Playing.", [1500 - scroll[0], 80 - scroll[1]], (0, 0, 0))
            
                tile_rects.clear()

                levels = load_map(f"level/level0{level}")

                tilemap.change_map(levels)
                tilemap.draw(screen, scroll)

                player.update(images, tile_rects, scroll)
                player.draw(screen, scroll)
                
            if stayCount >= 500:
                congrulotion_fade.fade(screen)
            if stayCount >= 650:
                pg.mouse.set_visible(True)
                draw_text(erfanFont, "Created By: Hamidreza", [width / 2, 200])
                if congrulotion_button.draw(screen):
                    run = False
                    exit()
                

        if level != 3:
            draw_text(font, f"Gems: {player.gems}", [70, 35], (0, 0, 0))
            healthBar.draw(screen, player.health)

        # Screen Fade
        play_fade.fade(screen)

        if player.alive == False:
            death_count += 1
            pg.mouse.set_visible(True)
            a = Button([320, 300], "Exit", (255, 170, 0), (196, 60, 0), (0, 0, 0))
            death_fade.fade(screen)

            if death_count >= 150:
                draw_text(erfanFont, "You Are Dead!", [width/2, 200], (0, 0, 0))
                if a.draw(screen):
                    run = False

        if level_compalte:
            level += 1
            if level <= MAX_LEVELS:
                levels = load_map(f"level/level0{level}")
                tilemap.change_map(levels)
                tilemap.draw(screen, scroll)

    pg.display.update()
    clock.tick(60)

pg.quit()
