class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                return [dict[nums[i]], i]
            dict[target - nums[i]] = i
