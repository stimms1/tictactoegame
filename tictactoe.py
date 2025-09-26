def printMatrix():
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])


def replace(symbol, xIntercept, yIntercept):
    matrix[xIntercept][yIntercept] = symbol
    printMatrix()

def reset_matrix():
    """Reset the matrix to empty values."""
    global matrix
    matrix = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    return matrix

def playTurn(symbol, oppositeSymbol):
    loop = True
    while loop == True:
        print(f"{symbol}'s turn!")
        xIntercept = int(input("What coordinate in the X axis? "))-1
        yIntercept = int(input("What coordinate in the Y axis? "))-1
        if matrix[xIntercept][yIntercept] == symbol or matrix[xIntercept][yIntercept] == oppositeSymbol:
            print("Invalid input!")
        else: 
            replace(symbol, xIntercept, yIntercept)
            loop = False
    
def checkWinner(matrix, symbol):
    if (matrix[0][0] == symbol and matrix[0][1] == symbol and matrix[0][2] == symbol) or (matrix[1][0] == symbol and matrix[1][1] == symbol and matrix[1][2] == symbol) or (matrix[2][0] == symbol and matrix[2][1] == symbol and matrix[2][2] == symbol) or (matrix[0][0] == symbol and matrix[1][0] == symbol and matrix[2][0] == symbol) or (matrix[0][1] == symbol and matrix[1][1] == symbol and matrix[2][1] == symbol) or (matrix[0][2] == symbol and matrix[1][2] == symbol and matrix[2][2] == symbol) or (matrix[0][0] == symbol and matrix[1][1] == symbol and matrix[2][2] == symbol) or (matrix[0][2] == symbol and matrix[1][1] == symbol and matrix[2][0] == symbol):
        return True
    else:
        return False
    
def checkDraw(matrix):
    for row in matrix: 
        for cell in row:
            if cell == '_':
                return False
    return True

def randomizer():
    return random.randint(0,1)

matrix = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

if __name__ == "__main__":
    import random

    
    randomizer = randomizer()
    isThereWinner = False

    printMatrix()

    symbol = 'X'
    opposite = 'O'
    if randomizer == 1:
        print("O goes first!")
        symbol = 'O'
        opposite = 'X'
    else: 
        print("X goes first!")

    while checkWinner(matrix, symbol) == False and checkWinner(matrix, opposite) == False:
        playTurn(symbol, opposite)
        symbol, opposite = opposite, symbol
        if checkWinner(matrix, symbol) == True:
            print(f"{symbol} wins!")
            reset_matrix()
            printMatrix()
            break
        elif checkWinner(matrix, opposite) == True:
            print(f"{opposite} wins!")
            reset_matrix()
            printMatrix()
        else:
            if checkDraw(matrix):
                print("It's a tie!")
                reset_matrix()
                break





