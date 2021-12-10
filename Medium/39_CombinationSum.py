class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lownum = candidates[0]
        output = []
        for i in range(len(candidates)-1,-1,-1):
            if candidates[i] == target:
                output.append([target])
            elif candidates[i] + lownum > target:
                continue
            else:
                subcombos = self.combinationSum(candidates[:i+1], target-candidates[i])
                for subcombo in subcombos:
                    subcombo.append(candidates[i])
                    output.append(subcombo)
        return output
