# 2
import numpy as np
from random import randrange
from math import ceil

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

def inputMatrix():
    print("Enter number of rows: ")
    N = getPositiveNumber(True)
    print("Enter number of columns: ")
    M = getPositiveNumber(True)

    matrix = np.zeros((N, M))

    print("Use 'Enter' to input the matrix")

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
    print("Input range using 'Enter'")
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
                operationsCounter += 3
    print("matrix sort operationsCounter = ", operationsCounter)
    print("SORTED MATRIX:\n", matrix)
    return matrix

def arrayBinarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return arrayBinarySearch(arr, l, mid-1, x)
        else:
            return arrayBinarySearch(arr, mid + 1, r, x)
    else:
        return -1

def MatrixbinarySearch(matrix, srchVal):
    found = False

    rows = len(matrix)
    cols = len(matrix[0])

    size = rows * cols

    i = len(matrix) // 2
    j = len(matrix[0]) // 2

    i_srch = 0
    j_srch = 0

    while found == False:
        if srchVal >= matrix[i][0] and srchVal <= matrix[i][cols-1]:
            i_srch = i
            found = True
        elif srchVal<=matrix[i][0]:
            i //= 2 
            if i == 0:
                i_srch = 0
                found = True
        elif srchVal>=matrix[i][cols-1]:
            i = ceil(i+i/2)
            if i == rows-1:
                i_srch = i
                found = True
    j_srch = arrayBinarySearch(matrix[i_srch], 0, cols-1, srchVal)
    if j_srch == -1:
        return "value not found"

    return i_srch, j_srch


def main():
    print("Hello, you have 2 options to run the programm:\n\
        option 1 - input matrix;\n\
        option 2 - randomly generate matrix, specifying the values range limites\n\
        if you want to to choose option 1, type '1'\n\
        if you want to to choose option 2, type '2'\n\
        to exit, just type 'exit'")

    while True:
        option = input()
        Exit(option)
        if option == '1':
            MatrixA = inputMatrix()
            searchValue = int(input("Enter a value, you want to search: "))
            Exit(searchValue)
            resultIndices = MatrixbinarySearch(sortMatrix(MatrixA), searchValue)
            break
        elif option == '2':
            MatrixA = generateMatrix()
            searchValue = int(input("Enter a value, you want to search: "))
            Exit(searchValue)
            resultIndices = MatrixbinarySearch(sortMatrix(MatrixA), searchValue)
            break
        else:
            print("you have only 2 options, try again: ")
            continue

    print("indeces of value, you search: ", resultIndices)


main()
