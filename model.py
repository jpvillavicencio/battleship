from constants import Status

class Battleship:
    def __init__(self, x, y, length, orientation):
        self.x = x
        self.y = y
        self.length = length
        self.orientation = orientation
        # self.health = health

class Board:
    def __init__(self, size):
        self.size = size
        self.board = []

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = Status.EMPTY
        
class Player:
    def __init__(self, name):
        self.name = name

