def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left,right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return helper(left.left,right.right) and helper(left.right,right.left)
        return helper(root.left,root.right) if root else True



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res = True
        if root:
            res = self.helper(root.left, root.right)
        return res
    
    def helper(self,A,B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        if A.val != B.val:
            return False
        
        return self.helper(A.left,B.right) and self.helper(A.right,B.left)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        res = True
        if root:
            res = self.helper(root.left, root.right)
        return res
    
    def helper(self,A,B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        if A.val != B.val:
            return False
        
        return self.helper(A.left,B.right) and self.helper(A.right,B.left)

