class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        num_dict = {}

        for i in nums:
            num_dict[i] = True
        for i in num_dict:
            if i - 1 not in num_dict:
                count = 1
                next = i + 1
                while next in num_dict:
                    next += 1
                    count += 1
                longest = max(longest, count)
        return longest