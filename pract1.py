#6
def calc(N):
	if N == 0:
		return 0
	elif N == 1:
		return 1
	elif N == 2:
		return 2
	elif N == 3:
		return 4
	return calc(N - 1) + calc(N - 2) + calc(N - 3)

def isNumber(N):
	try:
		int(N)
		return True
	except:
		return False

def isPositive(N):
  	return N >= 0

def getNumOfRoutes():
	N = input("Enter number of routes :")
	
	if not isNumber(N):
		print("Value should be a number")
		return 

	if not isPositive(int(N)):
		print("Value should be positive")
		return

	return calc(int(N))

result = getNumOfRoutes()

print(result)
