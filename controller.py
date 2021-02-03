from model import Battleship, Board, Coord
from constants import Status, Orientation

class GameController:
    def __init__(self, board):
        self.board = board
        self.resetBoard()


    def resetBoard(self):
        self.board.board.clear()
        for x in range(self.board.size):
            for y in range(self.board.size):
                self.board.board.append(Coord(x, y))
        return self.board

    def getCoord(self, x, y):
        for coord in self.board.board:
            if coord.x == x and coord.y == y:
                return coord

    def setCoord(self, x, y, status):
        for coord in self.board.board:
            if coord.x == x and coord.y == y:
                coord.update(status)
                return coord
            
    def printBoard(self):
        statusMap = {
            Status.EMPTY: "-",
            Status.SHIP: "O",
            Status.MISSED: "M",
            Status.HIT: "X"
        }
        _board = []
        _row = []
        for r in range(self.board.size):
            for coord in self.board.board:
                if coord.x == r:
                    _row.append(statusMap[coord.status])
            _board.append(_row[:])
            _row.clear()
        print(" ", *[r for r in range(self.board.size)])
        for i, row in enumerate(_board):
            print(i, " ".join(row))
        return self.board

    def place(self, ship):
        # check if ship fits
        if ship.length+ship.x > self.board.size or ship.length+ship.y > self.board.size:
            raise Exception("ERR: Ship is too big")
        
        # check if space is occupied
        for l in range(ship.length):
            if self.getCoord(ship.x+l, ship.y).status != Status.EMPTY:
                raise Exception("ERR: Coordinate is occupied")

        if ship.orientation == Orientation.VERTICAL:
            for l in range(ship.length):
                self.setCoord(ship.x+l, ship.y, Status.SHIP)
        else:
            for l in range(ship.length):
                self.setCoord(ship.x, ship.y+l, Status.SHIP)

    def attack(self, x, y):
        coord = self.getCoord(x, y)
        if coord:
            if coord.status == Status.EMPTY:
                self.setCoord(x, y, Status.MISSED)
                return "missed"
            elif coord.status == Status.SHIP:
                self.setCoord(x, y, Status.HIT)
                return "hit"
            elif coord.status == Status.MISSED or coord.status == Status.HIT:
                return "already attacked"
            else:
                return "error"


class BattleshipController:
    def __init__(self, ship):
        self.ship = ship
        