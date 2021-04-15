class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #函数内部的小的递归函数，作用是在大的函数中求值（树的层数）
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        #大函数递归终止条件
        if not root:
            return True
        '''
        小函数的root.left一层层向下走，一直走到叶节点return 0了，返回R上一层，此时root.right也是叶节点（如果是满二叉树）
        也是return 0，返回上一层，取max+1。此时一个倒数第二层的height（root.left）算出结果。返回倒数第三层，
        开始第三层的height（root.right）。。。。一直到根节点的左子树全部算完，得到height（left），开始根节点的右子树，
        判断根节点层树是否相差1。然后将根节点的左右节点重复此过程。总的流程是根节点左右子树是否超过1，
        然后调用大函数自身self.isBalanced(root.left)，但是不知道此时的self.isBalanced(root.left)，只知道是否相差1，
        又到下一层，一直到倒数第二层得到了答案。然后运行倒数第二层的self.isBalanced(root.right)，得到答案，回到倒数三层，
        直到回到根节点判断是否所有的都是True
        '''
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

#这个和上面的一模一样，上面的height和这个depth都是辅助的递归函数，可以选择嵌套，也可以选择另写一个方法（但是在调用时要加self）
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

import pytorch




