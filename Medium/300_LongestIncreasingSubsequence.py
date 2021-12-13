class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        record = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums), 1):
                if nums[i] < nums[j]:
                    record[i] = max(record[i], record[j]+1)
        return max(record)
