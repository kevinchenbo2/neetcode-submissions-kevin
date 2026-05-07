# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def traverse(root, left, right):
            if not root:
                return True
            
            if root.val >= right or root.val <= left:
                return False
            
            return traverse(root.left, left, root.val) and traverse(root.right, root.val, right)

        return traverse(root.left, float("-inf"), root.val) and traverse(root.right, root.val, float("inf"))
        
        
            

        