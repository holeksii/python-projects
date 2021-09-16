#6
def isNonDecreaseSorted(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def isNonIncreaseSorted(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

def deleteElements(arr):
    if (isNonDecreaseSorted(arr)) or (isNonIncreaseSorted(arr)):
        return arr
    else:
        m = len(arr) // 4
        for i in range(1, m + 1):
            arr.pop(4 * i - i)
    return arr

def isNumber(N):
	try:
		int(N)
		return True
	except:
		return False

def isPositive(N):
  	return N >= 0

def CreateArray():
    arr = []
    N = input("Enter number of elements: ")
  
    if not isNumber(N):
        print("Value should be a number")
        exit()

    N = int(N)

    if not isPositive(N):
        print("Value should be positive")
        exit()

    print("Enter array: ")

    for i in range(0, N):
        elem = input()
        isNumber(elem)
        arr.append(float(elem))
    return arr
result = deleteElements(CreateArray())

print(result)
