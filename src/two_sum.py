class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i,val in enumerate(nums):
            if (target-val) in sum_map:
                return [sum_map[target-val],i]
            else:
                sum_map[val] = i