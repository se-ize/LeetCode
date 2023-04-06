class Solution(object):
    def twoSum(self, nums, target):
        memo = {}
        for i, v in enumerate(nums):
            memo[v] = i
        for i, v in enumerate(nums):
            needed_number = target - v
            if needed_number in memo and i != memo[needed_number]:
                return (i, memo[needed_number])