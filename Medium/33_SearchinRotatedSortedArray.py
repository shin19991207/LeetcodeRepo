class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            if nums[start] <= nums[middle]:
                if target < nums[middle] and target >= nums[start]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if target < nums[middle] or target > nums[end]:
                    end = middle - 1
                else:
                    start = middle + 1
        return -1
    
