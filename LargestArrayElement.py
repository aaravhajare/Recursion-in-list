
def largest(a) :

    l = len(a) 

    if l == 1 :
        return a[0]

  
    return  max(a[0],largest(a[1 :]))
    


b = [1,21,2,32,3,4,3,2,32,423,42,34,23]
print(largest(b))