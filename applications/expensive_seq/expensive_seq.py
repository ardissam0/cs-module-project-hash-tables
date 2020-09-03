# Your code here


def expensive_seq(x, y, z, cache = dict()):

    # base case for early exit
    if x  <= 0:
        return y + z

    # if not in cache then put them in the cache
    # add them together
    if (x, y, z) not in cache:
        add1 = expensive_seq( x - 1, y + 1, z, cache)
        add2 = expensive_seq( x - 2, y + 2, z * 2, cache)
        add3 = expensive_seq( x - 3, y + 3, z * 3, cache)
        cache[(x, y, z)] = add1 + add2 + add3
        return cache[(x, y, z)]

    #else if they are already in there, return them
    else:
        return cache[(x, y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
