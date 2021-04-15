#双层for循环，O(n**2),暴力循环
def twoSum1(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(twoSum1([2,2,11,15],4))

#使用一层for循环
def twoSum2(nums,target):
    n = len(nums)
    for x in range(n):
        a = target - nums[x]
        if a in nums: # 判断a有没有在nums数组里
            y = nums.index(a) # 有的话，那么用index获取到该数字的下标
            if x != y:
                return [x,y]
                '''
				if x == y: 
					continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
				else: # 否则就返回结果
					return x,y 
					break
			else: 
				continue # 上面的条件都不满足就跳过，进行下一次循环
            '''
print(twoSum2([2,2,6,7,11,15],4))

#模拟哈希，使用字典来查询
def twoSum3(nums,target):
    hashmap={}
    for index,num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num],index]
        #下面这句只能在下面，如果在上面，就会返回错误的[0,0]
        hashmap[num] = index
        

print(twoSum3([1,2,3,4,2],5))
print(twoSum3([2,7,2,11,15],4))

'''
以上所有解法都只有一种答案，如果想把所有答案找出来
'''
def twoSum4(nums,target):
        d = {}
        res = []
        for k,v in enumerate(nums):
            if target-v in d:
                res.append([d[target-v],k])
            d[v] = k
        return res
print(twoSum4([1,2,3,4,2],5))

