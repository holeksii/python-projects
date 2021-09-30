import numpy as np
from random import randrange


def isNumber(N):
	try:
		int(N)
		return True
	except:
		return False


def isPositive(N):
  	return N >= 0


def Exit(val):
    if val != 'exit':
        print("If you want to exit, type 'exit'")
    else:
        exit()


def getPositiveNumber(m):
# if m == True, function return positive number,
# if m == False, function returns number
    while True:
        num = input()
        if not isNumber(num):
            print("Value should be a number")
            Exit(num)
            continue
        num = int(num)
        if m == True:
            if not isPositive(num):
                print("Value should be a positive number")
                Exit(num)
                continue
        break
    return num


def enterMatrix():
    print("Enter number of rows: ")
    N = getPositiveNumber(True)
    print("Enter number of columns: ")
    M = getPositiveNumber(True)

    matrix = np.zeros((N, M))

    print("Please enter matrix element by element")

    for i in range(N):
        for j in range(M):
            matrix[i][j] = getPositiveNumber(False)

    print("YOUR MATRIX: ", matrix)
    return matrix


def generateMatrix():
    print("Enter number of rows: ")
    N = getPositiveNumber(True)
    print("Enter number of columns: ")
    M = getPositiveNumber(True)
    matrix = np.zeros((N, M))  
    print("Input range number by number")
    while True:
        a = getPositiveNumber(False)
        b = getPositiveNumber(False)
        if (b < a):
            print("The lower limit cannot be bigger than the upper limit, try again:")
            continue
        break
    for i in range(N):
        for j in range(M):
            matrix[i][j] = randrange(a, b)
    
    print("YOUR MATRIX:\n", matrix)
    return matrix


def sortMatrix(matrix):
    operationsCounter = 0
    row = len(matrix)
    col = len(matrix[0])

    size = row * col
     
    for i in range(0, size):
        for j in range(0, size-1):
            if ( matrix[j//col][j % col] > matrix[(j + 1)//col][(j + 1)% col] ):
                operationsCounter += 1

                temp = matrix[j//col][j % col]
                matrix[j//col][j % col] = matrix[(j + 1)//col][(j + 1)% col]
                matrix[(j + 1)//col][(j + 1)% col] = temp
                operationsCounter += 1
    print("matrix sort operationsCounter = ", operationsCounter)
    print("SORTED MATRIX:\n", matrix)
    return matrix


def matrixBinarySearch(matrix, srchVal):
    cols = len(matrix[0])
    rows = len(matrix)
    lo = 0
    hi = rows * cols - 1
    while lo <= hi:
        mi = lo + ((hi-lo) >> 1)
        row = mi // cols
        col = mi % cols
        if(matrix[row][col] == srchVal): 
            return row, col
        elif(matrix[row][col] > srchVal):
            hi = mi - 1
            # return matrixBinarySearch(matrix, srchVal, hi, lo)
        else:
            lo = mi + 1
            # return matrixBinarySearch(matrix, srchVal, hi, lo)
    return 'Value not found'


def menu():
    options = {'1 - Enter matrix' : enterMatrix,
               '2 - Randomly generate matrix, specifying the values range limites': generateMatrix,
               '3 - Exit' : exit}

    print("Hello :)\nYou are in Menu, choose one option to continue:")

    while True:
        for key in options.keys():
            print(key)
        option = input()
        for i in options.keys():
            if option == i[0]:
                return options[i]()
        print('Oops!\nTry to choose from available options:')


def getIndecesOfSearchValue():
    matrix = sortMatrix(menu())
    print("Enter a value, you want to search: ")
    searchValue = getPositiveNumber(False)
    Exit(searchValue)
    return matrixBinarySearch(matrix, searchValue)


while True:
    resultIndices = getIndecesOfSearchValue()
    print("Indeces in sorted matrix of value, you search: ", resultIndices)
