def fixedPoint(A):
    i = 0
    while i < len(A):
        if i==A[i]:
            return i
        i+=1
    else:
        return -1

print(fixedPoint([-10,-5,0,3,7]))

def fixedPoint2(A):
    for i in range(len(A)):
        if A[i]==i:
            return i
    return -1

print(fixedPoint2([-10,-5,0,3,7]))
print(fixedPoint2([0,1,2,3,7]))
print('fuck you all')

