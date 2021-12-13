class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start <= end:
            middle = (start+end) // 2
            if nums[middle] == target:
                return True
            if nums[start] < nums[middle]:
                if target < nums[middle] and target >= nums[start]:
                    end = middle - 1
                else:
                    start = middle + 1
            elif nums[start] == nums[middle]:
                # binary search is not helpful
                start += 1
                continue;
            else:
                if target > nums[middle] and target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
                
        return False
