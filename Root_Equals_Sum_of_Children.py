# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return False
        else:
            if (root.right.val + root.left.val == root.val):
                return True
            else:
                return False