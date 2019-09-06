#!/usr/bin/env python3

# +==========================================================================================+
# |                                                                                          |
# |    The cube of any integer is always 0, -1 or +1 modulo 9                                |
# |                                                                                          |
# +==========================================================================================+
assert 0 == len([x*x*x for x in range(-100000, 100000) if (x*x*x % 9) not in {0, 1, 8}])


# +==========================================================================================+
# |                                                                                          |
# |    The digital root (in base 10) of a positive integer is its difference from the        |
# |    largest multiple of 9 that is less than the number itself                             |
# |                                                                                          |
# +==========================================================================================+
def digitalRoot(n):
    """returns a tuple consisting of the digital root of a number alongside its additive persistence
       see: https://en.wikipedia.org/wiki/Digital_root
       >>> digitalRoot(65536)
       (7, 2)
    """
    def _digitalRoot(n, additivePersistence):
        v = sum(map(int, [ x for x in str(n) ]))
        if (v>9):
            return _digitalRoot(v, additivePersistence+1)
        else:
            return (v, additivePersistence)

    return _digitalRoot(n, 1)


def digitalRootWithFormula(n):
    if (n % 9 == 0):
        return 9;
    else:
        return n - 9*(n // 9)

# this is more clever
def digitalRootWithFormula2(n):
    return n - 9*((n-1) // 9)
    

for f in [digitalRootWithFormula, digitalRootWithFormula2]:
    assert len (list(filter(lambda n: digitalRoot(n)[0]!=f(n), range(1, 100*1000)))) == 0

def drOfSumsAndProducts():
    """the digital root of a sum or product is the digital root of the sum or product of the digital roots"""
    dr = lambda n: digitalRoot(n)[0]
    for a in range(1, 100000, 2732):
        for b in range(1, 1000, 13):
            assert dr(a+b)==dr(dr(a)+dr(b))
            assert dr(a*b)==dr(dr(a)*dr(b))
drOfSumsAndProducts()            

def digitalRootsOfCubes():
    "the digital roots of positive cubes are always 1, 8 and 9; and they repeat in that order"
    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
                yield tuple(val)
    drOfCubes = [ digitalRoot(n*n*n)[0] for n in range(1, 10000)]
    drOfCubesGrouped = group(drOfCubes, 3)
    s = set([*drOfCubesGrouped])
    assert len(s)
    assert next(iter(s))==(1,8,9)
    

digitalRootsOfCubes()


    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
