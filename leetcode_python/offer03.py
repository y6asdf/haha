#暴力排序，暴力遍历
def findRepeatNumber(nums):
    nums = sorted(nums)
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            return nums[i]

print(findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))

#和上述方法一样的
def findRepeatNumber1(nums):
    nums.sort()
    pre = nums[0]
    for index in range(1, len(nums)):
        if pre == nums[index]:
            return pre
        pre = nums[index]
print(findRepeatNumber1([2, 3, 1, 0, 2, 5, 3]))

#哈希表
def findRepeatNumber2(nums):
    hashtable={}
    for i in nums:
        if i not in hashtable:
            hashtable[i]=0
        else:
            return i
print(findRepeatNumber2([2, 3, 1, 0, 2, 5, 3]))




