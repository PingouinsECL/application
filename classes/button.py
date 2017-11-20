class Button:

    def __init__(self, picture, picture_hover, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.background = picture
        self.background_hover = picture_hover

    def show(self, win, cur):
        if self.hover(cur):
            win.blit(self.background_hover, [self.x, self.y])
        else:
            win.blit(self.background, [self.x, self.y])

    def hover(self, cur):
        x_cur, y_cur = cur
        return 0 < x_cur - self.x < self.background.get_width() and 0 < y_cur - self.y < self.background.get_height()
