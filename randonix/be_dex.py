import random
import math
def randintx(a, b, seed=False) :
    i = random.randint(1, math.factorial(100))
    random.seed(i)
    
    if seed :
        print(f"seed:  {i} \n\nnum:")
    else :
        pass
    return random.randint(a, b)
