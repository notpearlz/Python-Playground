
import random

def main():
    pass




def startGame():
    board = [];
    size = 100;


    board = fillBoard(board, size);
    pass

def hasNeighbor():
    pass




def fillBoard(board, size):
    for i in range(size):
        board[i] = ''
    
def populateCell():
    cellChance = 5
    num = random.randint(0,100)

    
    if(num <= cellChance):
        return True
    else:
        return False



main()
