
def sort(a) :

    l = len(a)

    if l == 0 or l == 1 :
        return True
    
    return a[0] <= a[1] and sort(a[1 :])

b = [1,3,4,2]



if sort(b) :
    print("yes its a sorted array")

else :
    print("its not a sorted array")