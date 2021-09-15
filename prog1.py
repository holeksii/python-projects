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

def isNumber(n):
	try:
		int(n)
	except ValueError:
		print("Value should be number")
		exit()

def isPositive(N):
  return N >= 0

def CreateArray():
    arr = []
    N = int(input("Enter number of elements : "))
  
    isNumber(N)

    if not isPositive(N):
        print("Value should be positive")
        exit()

    print("Enter array:")
  
    for i in range(0, N):
        elem = input()
        isNumber(elem)
        arr.append(float(elem))
    return arr

print(deleteElements(CreateArray()))
