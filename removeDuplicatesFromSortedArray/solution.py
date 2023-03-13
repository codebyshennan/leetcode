# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = -111
        for i, num in enumerate(nums):
            if num == tmp:
                nums[i] = -111
            else:
                tmp = num

        nums[:] = [i for i in nums if i != -111]
        
        return len(nums)
        
        # other solutions
        # nums[:] = sorted(set(nums))
        # return len(nums)   