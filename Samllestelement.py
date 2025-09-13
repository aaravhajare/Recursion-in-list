import math as m 

def smallest(a) :

    l = len(a)

    if l == 1:
        return a[0]

    return min(a[0],smallest(a[1:]))

b = [2,3,4,5]
print(smallest(b))