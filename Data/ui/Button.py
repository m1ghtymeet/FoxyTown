import pygame as pg

class Button:
    def __init__(self, pos, text, bg, bg_b, fg):
        self.text = text
        self.color_bg = bg
        self.color_fg = fg
        self.color_bg_b = bg_b
        self.rect = pg.Rect(pos[0], pos[1], 150, 50)
        self.rect_back = pg.Rect(pos[0], pos[1], 150, 50)
        self.font = pg.font.Font("Font/F.ttf", 25)
        self.clicked = False
        self.y = pos[1]

    def draw_text(self, surf, text, pos):
        image = self.font.render(text, False, self.color_fg, (0, 0, 0))
        image.set_colorkey((0, 0, 0))
        surf.blit(image, (pos[0] - (image.get_width() / 2), pos[1]))

    def draw(self, surf):
        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.rect.y = self.y
            if pg.mouse.get_pressed()[0] == 1:
                self.clicked = True
                action = True
        else:
            self.rect.y = self.y - 10

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 0:
                self.clicked = False

        pg.draw.rect(surf, self.color_bg_b, self.rect_back)
        pg.draw.rect(surf, self.color_bg, self.rect)
        self.draw_text(surf, self.text, [self.rect.centerx, self.rect.centery - 10])

        return action