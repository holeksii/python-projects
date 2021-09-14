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
	except:
		print("Value should be number")
		exit()


def CreateArray():
    arr = []
    N = int(input("Enter number of elements : "))
  
    isNumber(N)

    print("Enter array:")
  
    for i in range(0, N):
        try:
            elem = float(input())
        except ValueError:
            print("Value should be number")
            return arr
        arr.append(elem)
    return arr



print(deleteElements(CreateArray()))
