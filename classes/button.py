from math import sqrt
class Button:

    def __init__(self, picture, picture_hover, pos,type):
        self.x = pos[0]
        self.y = pos[1]
        self.type = type          # type = 0 si la case est carré, type = 1 si la case hexagonale
        self.background = picture
        self.background_hover = picture_hover

    def show(self, win, cur):
        if self.hover(cur):
            win.blit(self.background_hover, [self.x, self.y])
        else:
            win.blit(self.background, [self.x, self.y])

    def hover(self, cur):
        x_cur, y_cur = cur
        a = self.background.get_width()
        xc, yc = self.x+a/2, self.y+a/2
        h=sqrt(2)*a/(2+sqrt(2)) 
        # when hovered
        if self.type == 1:
            if xc-a/2<= x_cur <= xc+a/2  and yc-a/2 <= y_cur <= yc+a/2 and y_cur >= -x_cur + yc +xc - (a+h)/2 and y_cur >= x_cur + yc - xc - (a+h)/2 and y_cur <= -x_cur + yc +xc + (a+h)/2 and y_cur <= x_cur + yc -xc +(a+h)/2:
                print('non')
            else:
                print("Vous n'êtes pas sur la case") 
                
        else:
            return 0 < x_cur - self.x < self.background.get_width() and 0 < y_cur - self.y < self.background.get_height()
