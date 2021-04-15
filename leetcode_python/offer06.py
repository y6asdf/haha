'''
实际上head是ListNode的实例，
head有两个属性，
一个是head.val，查看当前的值，
一个是head.next,查看下一个值
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
递归法 
利用递归将头结点移动到末端，然后回溯，依次将节点的值放入到列表中，既可以实现链表中的值倒序输出。

递归方式：

递归终止条件：当head=None时，说明链表已经到结尾了，返回空的列表。
递归递推条件：访问下一个节点head=head.next。
回溯方式：下一步递归返回结果list + [head.val]（不同的语言有不同的实现方式）。
复杂度分析

时间复杂度O(N)：遍历链表N次
空间复杂度O(N)：系统递归需要使用O(N)这么大的栈空间
'''
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return self.reversePrint(head.next) + [head.val] if head else []



'''
辅助栈法

对于题目中的单项链表来说，只能从前往后访问每个节点，题目要求倒序输出各个节点的值，很容易就可以联想到栈这种先进后出的数据结构了。如果使用Python的话，在遍历一个链表的时候，将值依次放入到一个list中，遍历结束后，翻转list输出即可。

复杂度分析

时间复杂度O(N)：list添加数据N次

空间复杂度O(N)：list存储结果O(N)这么大的空间
'''
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

'''
利用堆栈先进后出的特点，先依次将元素压入堆栈中，然后将所有元素从堆栈中弹出，即可实现反转

时间复杂度：O(n)，push的间复杂度为 O(n)，pop的间复杂度为 O(n)。
空间复杂度：O(n)，使用了额外的 res 和 堆栈。
'''
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head: # push
            stack.append(head.val)
            head = head.next
        res = []
        while stack: # pop
            res.append(stack.pop())
        return res


