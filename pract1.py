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
	while True:
		N = input("Enter number of routes :")
		
		if not isNumber(N):
			print("Value should be a number")
			continue

		N = int(N)
		
		if not isPositive(N):
			print("Value should be positive")
			continue

		return calc(N)

result = getNumOfRoutes()

print(result)
