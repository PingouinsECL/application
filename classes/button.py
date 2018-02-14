from math import sqrt

def is_in_triangle(x, y, x_1, y_1, x_2, y_2, x_3, y_3):
    v0 = [x_3 - x_1, y_3 - y_1]
    v1 = [x_2 - x_1, y_2 - y_1]
    v2 = [x - x_1, y - y_1]

    dot00 = v0[0]**2 + v0[1]**2
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]

    invDenom = 1/(dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom
    
    return u>=0 and v>=0 and u+v<1

class Button:

    def __init__(self, picture, picture_hover, pos, ctype):
        self.x = pos[0]
        self.y = pos[1]
        self.type = ctype          # type = 0 si la case est carré, type = 1 si la case hexagonale
        self.background = picture
        self.background_hover = picture_hover

    def show(self, win, cur):
        if self.hover(cur):
            win.blit(self.background_hover, [self.x, self.y])
        else:
            win.blit(self.background, [self.x, self.y])

    def hover(self, cur):
        x_cur, y_cur = cur

        """
        xc, yc = self.x+a/2, self.y+a/2
        h=sqrt(2)*a/(2+sqrt(2)) 
        # when hovered
        if self.type == 1:
            return xc-a/2<= x_cur <= xc+a/2  and yc-a/2 <= y_cur <= yc+a/2 and y_cur >= -x_cur + yc +xc - (a+h)/2 and y_cur >= x_cur + yc - xc - (a+h)/2 and y_cur <= -x_cur + yc +xc + (a+h)/2 and y_cur <= x_cur + yc -xc +(a+h)/2
        """ 

        if self.type == 1:
            a = self.background.get_height()/2
            h = 3**0.5 * a / 2

            xc = self.x + h
            yc = self.y + a

            x0 = xc
            y0 = yc - a

            x1 = xc + h
            y1 = yc - a/2

            x2 = xc + h
            y2 = yc + a/2

            x3 = xc
            y3 = yc + a
            
            x4 = xc - h
            y4 = yc + a/2

            x5 = xc - h
            y5 = yc - a/2

            return (is_in_triangle(x_cur, y_cur, xc, yc, x0, y0, x1, y1) or \
                    is_in_triangle(x_cur, y_cur, xc, yc, x1, y1, x2, y2) or \
                    is_in_triangle(x_cur, y_cur, xc, yc, x2, y2, x3, y3) or \
                    is_in_triangle(x_cur, y_cur, xc, yc, x3, y3, x4, y4) or \
                    is_in_triangle(x_cur, y_cur, xc, yc, x4, y4, x5, y5) or \
                    is_in_triangle(x_cur, y_cur, xc, yc, x5, y5, x0, y0))      
        else:
            return 0 < x_cur - self.x < self.background.get_width() and 0 < y_cur - self.y < self.background.get_height()

    def modify_image(self,image):
        self.background=image