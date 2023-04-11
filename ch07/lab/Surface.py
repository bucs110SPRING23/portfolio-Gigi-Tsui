from Rectangle import Rectangle

class Surface:
    def __init__ (self, filename, x,y,h,w):
        self.image = filename
        self.rect = Rectangle(abs(x),abs(y),abs(h),abs(w))

    def getRect(self):
        return self.rect