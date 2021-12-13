# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(root, s):
            if not root:
                return 
            if not root.right and not root.left:
                output.append(s + str(root.val))
                return 
            else:
                s = s + str(root.val) + "->"
                helper(root.left, s[:])
                helper(root.right, s[:])
        output = []
        helper(root, "")
        return output
