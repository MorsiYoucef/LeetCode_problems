class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        temp=root.right
        root.right=root.left
        root.left=temp

        self.invertTree(root.right)
        self.invertTree(root.left)


        return root