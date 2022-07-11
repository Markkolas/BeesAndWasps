#This file describe the Queen class bee, only bee controlable by the player
import bees.bee as b

class Queen(b.Bee):
    speed = 10

    def __init__(self, x, y):
        b.Bee.__init__(self, x, y)
