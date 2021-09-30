import numpy as np
from random import randrange

def isNumber(N):
	try:
		int(N)
		return True
	except:
		    return False

def isPositive(N):
  	return N > 0

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

def EnterMatrixA():
    print("Please enter number of rows: ")
    N = getPositiveNumber()
    print("Please enter number of cols: ")
    M = getPositiveNumber()

    A = np.zeros((N, M))

    print("Please enter matrix element by element")

    for i in range(N):
        for j in range(M):
            A[i][j] = getPositiveNumber()
    return A

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

def newMatrixB(A):
    N = len(A)
    M = len(A[0])
    B = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            for f in range(i + 1):
                B[i][j] += A[f][j]
    return B

def Run(func):
    print("New Matrix:")
    return newMatrixB(func)

def menu():
    options = {'1 - Enter matrix' : EnterMatrixA,
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

while True:
    print(Run(menu()))
