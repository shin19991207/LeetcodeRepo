class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        output = []
        subs = []
        for i in range(len(nums)):
            subcombos = self.permute(nums[i+1:])
            for sub in subcombos:
                for j in range(len(sub)):
                    combo1 = sub[:j] + [nums[i]] + sub[j:]
                    if combo1 in subs:
                        break
                    combo2 = sub[j:] + [nums[i]] + sub[:j]
                    subs.append(combo1)
                    subs.append(combo2)
                    if len(combo1) == len(nums):
                        output.append(combo1)
                        output.append(combo2)
        return output
