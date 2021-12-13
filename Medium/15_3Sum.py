class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        added = set()
        output = []
        for i in range(len(nums)):
            first = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = first + nums[start] + nums[end]
                if sum == 0 and (first, nums[start], nums[end]) not in added:
                    output.append([first, nums[start], nums[end]])
                    added.add((first, nums[start], nums[end]))
                elif sum > 0:
                    end -= 1
                else:
                    start += 1
        return output
