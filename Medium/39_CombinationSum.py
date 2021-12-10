class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lownum = candidates[0]
        output = []
        for i in range(len(candidates)-1,-1,-1):
            if candidates[i] == target:
                output.append([target])
            # if current value + the smallest number in candidates is greater than target => there is no combination sum with this current value
            elif candidates[i] + lownum > target:
                continue
            else:
                # recurse on the sublist candidates[:i+1] to find the combination sum with this current value candidates[i]
                subcombos = self.combinationSum(candidates[:i+1], target-candidates[i])
                # for each sub-combination-sum-list, add the current value candidates[i] in it and append it to the output list
                for subcombo in subcombos:
                    subcombo.append(candidates[i])
                    output.append(subcombo)
        return output
