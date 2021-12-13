# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        self.helper(root, targetSum, [], output)
        return output
        
    def helper(self, root, sum, list, output):
        if not root:
            return
        list = list + [root.val]
        if not root.left and not root.right and root.val == sum:
            output.append(list)
            return
        else:
            self.helper(root.left, sum-root.val, list[:], output)
            self.helper(root.right, sum-root.val, list[:], output)
            return
