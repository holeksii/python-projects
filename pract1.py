#6
def calc(N):
	if N == 1:
		return 1
	elif N == 2:
		return 2
	elif N == 3:
		return 4
	return calc(N - 1) + calc(N - 2) + calc(N - 3)

def isNumber(N):
	try:
		int(N)
	except:
		print("Value should be number")
		exit()

def isPositive(N):
  return N >= 0

def getNumOfRoutes():
	print("Enter number of routes :")
	N = int(input())
	isNumber(N)

	if not isPositive(N):
		print("Value should be positive")
		exit()
	return calc(N)

print(getNumOfRoutes())
