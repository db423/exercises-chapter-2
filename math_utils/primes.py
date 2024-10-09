import math
def isprime(p):
    if p==1: return False
    for i in range(2,math.floor(p**1/2)+1):
        if p % i == 0:
            return False
    return True