from random import randrange


def linked_list(lst):
    for item in lst:
        yield item

def randomly_generate(a, b, N):
    for i in range(N):
        yield randrange(a,b,N)
