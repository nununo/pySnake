class Food(object):

    def __init__(self, xyVector, color):
        self.position = xyVector
        self.color = color
    
    def draw(self, game):
        game.draw_cell(*self.position.point, self.color)
