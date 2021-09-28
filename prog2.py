import numpy as np

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

def getPositiveNumber():
    while True:
        num = input()
        if not isNumber(num):
            Exit(num)
            print("Value should be a number")
            continue
        num = int(num)
        if not isPositive(num):
            Exit(num)
            print("Value should be a positive number")
            continue
        break
    return num

def CreateMatrixA():
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

def newMatrixB(A):
    N = len(A)
    M = len(A[0])
    B = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            for f in range(i + 1):
                B[i][j] += A[f][j]
    return B

def Run():
    return newMatrixB(CreateMatrixA())

def menu():
    options = {'1 - Run' : Run,
               '2 - Exit' : exit}
    
    print("Hello :)\nYou are in Menu, choose one option to continue:")

    while True:
        for key in options.keys():
            print(key)
        option = input()
        for i in options.keys():
            if option == i[0]:
                return options[i]()
        print('Oops!\nTry to choose from available options:')

print(menu())
