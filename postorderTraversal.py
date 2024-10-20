class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def poT(root):
            if not root:
                return 
            
            poT(root.left)
            poT(root.right)
            res.append(root.val)
        
        poT(root)

        return res