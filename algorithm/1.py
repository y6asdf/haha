'''
变位词判断：
heart & earth
'''
#逐字检查
def anagrmSolution1(s1,s2):
    alist = list(s2)
    pos1 = 0
    stillok = True
    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found = True
            else:
                pos2 +=1
        if found:
            alist[pos2] = None
        else:
            stillok = False
        pos1 +=1
    return stillok

print(anagrmSolution1('python','typhon'))
print(anagrmSolution1('bee','ebe'))

#排序比较
def anagrmSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    if alist1 == alist2:
        found = True
    else:
        found = False
    return found

print(anagrmSolution2('python','typhon'))

#计数比较
