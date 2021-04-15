'''
我的解法
'''
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for i in range(len(nums)):
           sums.append(sum(nums[:i+1]))
        return(sums)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums


def binarysearch(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
        
    return -1


def coinchange(coins,amount):
    memory = dict()
    if amount in memory:
        return memory[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = float('inf')
    for coin in coins:
        subproblem = coinchange(coins,amount-coin)
        if subproblem == -1:
            continue
        res = min(res,1+subproblem)
    memory[amount] = res if res != float('inf') else -1
    return memory[amount]


def l

