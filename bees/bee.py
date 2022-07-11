#Common attributes and methods for bees

class Bee:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return [self.x, self.y]
