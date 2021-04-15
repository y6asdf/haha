#冒泡排序
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(len(alist)-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist
#提前终止的冒泡排序
def bubbleSort(alist):
    change=True
    length=len(alist)-1
    while length > 0 and change:
        change=False
        for i in range(length):
            if alist[i] > alist[i+1]:
                change=True
                alist[i],alist[i+1]=alist[i+1],alist[i]
        length-=1
    return alist


#选择排序
def selectionSort(alist):
    for i in range(len(alist)-1,0,-1):
        positionMax=0
        for j in range(1,i+1):
            if alist[j] > alist[positionMax]:
                positionMax=j
        alist[i],alist[positionMax]=alist[positionMax],alist[i]
    return alist


#插入排序
def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue=alist[i]
        position=i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position]=alist[position-1]
            position-=1
        alist[position]=currentvalue
    return alist

#希尔排序
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print('sublistcount: ',sublistcount,'list: ',alist)
        sublistcount //= 2
    return alist
def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue=alist[i]
        position=i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position]=alist[position-gap]
            position-=gap
        alist[position]=currentvalue
    return alist

#快速排序
def quickSort(arr):
    return array if len(array) <=1 \
    else quickSort([i for i in arr[1:] if i <array[0]]) + array[0:1] + \
    quickSort([j for j in array[1:] if j >=array[0]])



