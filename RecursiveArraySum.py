
def add(a) :

    l = len(a) 

    if l == 1 :
        return a[0]
    
    return a[0] + add(a[1 :])

b = [1,2,3,4]

print(add(b))