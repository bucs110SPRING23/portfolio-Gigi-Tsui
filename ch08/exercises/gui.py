class Player:
  def __init__(self, pnum=1):
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small


class Bullet:
  def __init__(self, x, y, damage):
    self.x = x
    self.y = y
    self.speed = 5
    self.damage = damage
    self.fired = False


class block:
  def __init__(self,x,y,broken):
    self.x = x
    self.y = y
    self.broken = False

class Cloud:
  def __init__ (self,x,y,speed, move):
    self.x = x
    self.y = y
    self.speed = 10
    self.move = True
