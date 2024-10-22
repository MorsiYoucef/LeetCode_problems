# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def preOrder(root,left):
            if(not root):
                return
            preOrder(root.left, True)
            preOrder(root.right, False)

            if not root.left and not root.right and left:
                self.total += root.val
        
        preOrder(root, False)
        return self.total
        
        

        
        



        