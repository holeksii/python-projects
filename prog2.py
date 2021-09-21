# 6
import numpy as np

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

def getPositiveNumber():
    while True:
        num = input()
        if not isNumber(num):
            print("Value should be a number")
            Exit(num)
            continue
        num = int(num)
        if not isPositive(num):
            print("Value should be a positive number")
            Exit(num)
            continue
        break
    return num

def CreateMatrixA():
    print("Enter number of rows: ")
    N = getPositiveNumber()
    print("Enter number of cols: ")
    M = getPositiveNumber()

    A = np.zeros((N, M))

    print("Use enter to input the matrix")

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

result = newMatrixB( CreateMatrixA())
print(result)
