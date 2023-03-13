# Two Sum

[LC](https://leetcode.com/problems/two-sum/description/)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a new set to store numbers
        # iterate thru the list and compute the difference
        # check if difference is in set, if not, add number to set
        store = {}

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in store:
                return [store[diff], index]
            else:
                store[nums[index]] = index
```
