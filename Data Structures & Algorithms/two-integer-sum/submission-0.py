class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            if i in d.keys():
                return [d[i], idx]
            diff = target - i
            d[diff] = idx

# 3, 0, 1, 4, 5
# t is 8
# d[5]=id 0
