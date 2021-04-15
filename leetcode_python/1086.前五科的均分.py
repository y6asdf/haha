def highFive(items):
    idlist = list(set(i for i,j in items))
    res = []
    for id in idlist:
        scorelist = []
        for ids,scores in items:
            if id ==ids:
                scorelist.append(scores)
        sums = sum(sorted(scorelist,reverse=True)[:5])
        res.append([id,int(sums/5)])    
    return res

print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))

def highFive2(items):
    from collections import defaultdict
    d = defaultdict(list)
    for i, score in items: # 只加最大的5个数进去
        if len(d[i]) >= 5:
            min_num = min(d[i]) 
            d[i].remove(min_num) # 抛弃最小数
            d[i].append(max(score, min_num))
        else:
            d[i].append(score)  
    return [[k, int(sum(v) / 5)] for k, v in d.items()]
print(highFive2([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
