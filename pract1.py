#6
def func(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    return func(N - 1) + func (N - 2) + func(N - 3)

def isNumber(n):
	try:
		int(n)
	except:
		print("Value should be number")
		exit()

N = input(int())
isNumber(N)
print("number of all routes: ")
print(func(N))
