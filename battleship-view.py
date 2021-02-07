from controller import GameController
from model import Board, Battleship, Coord
from constants import Orientation

def initialisePlayer():
    print("Player 1, enter your name: ", end="")
    player1 = input()
    print("Player 2, enter your name: ", end="")
    player2 = input()
    print("Welcome", player1, "and", player2)
    return player1, player2
    
def initialiseBoard():
    print("How big is your board? Input 1 value for n? ", end="")
    size = int(input())
    return size

def initialiseShip():
    ships = []
    while True:
        print("How big is your ship (1 x n)?", end="")
        length = int(input())
        print("What is the starting x coordinate?", end="")
        x = int(input())
        print("What is the starting y coordinate?", end="")
        y = int(input())
        while True:
            print("What's your ships orientation (1 = vertical, 2 = horizontal)?", end="")
            orientation = int(input())
            if orientation == 1 or orientation == 2:
                break
        while True:
            print("Do you want to add another ship(y/n)?", end="")
            addMore = input()
            if addMore == "y" or addMore == "n":
                break
        ships.append({
            "length": length,
            "x": x,
            "y": y,
            "orientation": orientation
        })
        if addMore == "n":
            break
    return ships

def playerAttack():
    print("What row do you want to attack?", end="")
    x = int(input())
    print("What column do you want to attack?", end="")
    y = int(input())
    return {"x": x, "y": y}

def main():
    # get players
    player1, player2 = initialisePlayer()
    # build board
    boardConfig = {
        "size": initialiseBoard()
        # "size": 5
    }
    board = Board(**boardConfig)
    gameController = GameController(board)

    # reset
    gameController.resetBoard()
    gameController.printBoard()

    # build battleship and place
    ships = initialiseShip()
    for ship in ships:
        gameController.place(Battleship(**ship))
        gameController.printBoard()
    
    # player attacks
    print(gameController.attack(**playerAttack()))
    gameController.printBoard()

if __name__ == "__main__":
    main()
