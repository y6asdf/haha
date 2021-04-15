class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:return ''
            if root.right or root.left:return str(root.val) + '(' + 
            helper(root.left)+ ')' + 
            ('('+helper(root.right)+')'if root.right else '')
            if not root.right and not root.left:return str(root.val)
    
        return helper(t)
        

        