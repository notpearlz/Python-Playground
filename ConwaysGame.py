
import random

def main():
    boardSize = 10

    board = fillBoard(boardSize)
    printBoard(board)




def startGame():
    board = [];
    size = 100;


    board = fillBoard(board, size);
    pass

def hasNeighbor():
    pass


def printBoard(board):
    size = len(board)

    for i in range(size):
        for j in range(size):
            print(board[i][j], end='')
        print();

    

def fillBoard(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('#')

    return board
            
    
def populateCell():
    cellChance = 5
    num = random.randint(0,100)

    
    if(num <= cellChance):
        return True
    else:
        return False



main()
