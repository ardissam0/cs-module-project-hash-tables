import random
import math

# intialize a cache
# to store data already found
cache = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # use cache to make things faster
    # if not in the cache
    # add them to the cache
    if (x, y) not in cache:
        cache[(x, y)] = slowfun_too_slow(x,y)

    # return them if you find them 
    return cache[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
