'''
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print(f'a,b,c={a,b,c}')
'''
'''
改进：
c=1000-a-b
'''
for a in range(0,1001):
    for b in range(0,1001):
        c=1000-a-b
        if a**2+b**2==c**2:
            print(f'a,b,c={a,b,c}')





