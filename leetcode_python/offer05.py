'''
由于字符串在python中是不可变量,所以第一步将其抓换成list
从头到尾开始扫描,如果当前字符为空格,则用'%20'替换
时间复杂度O(n),空间复杂度O(n)
'''
#str.join是指
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
jie = Solution()
jie.replaceSpace('fuck you')


'''先按空格分割，再把‘%20’.join'''
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        return '%20'.join(s)
jie = Solution()
jie.replaceSpace('fuck you')


'''
python内置的replace函数用来替换字符串中指定的字符
时间复杂度O(n),空间复杂度O(1)
'''
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ','%20')
jie = Solution()
jie.replaceSpace('fuck you hahah')


'''
先按空格分割，再用‘%20’.join
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.split(' ')
        return '%20'.join(s)
jie = Solution()
jie.replaceSpace('fuck you hahah')


'''
双指针移动+计数：这个方法的思路是:
首先遍历一次字符串s来统计有多少个空格
假设有m个空格,我们需要填充的%20占用三个字符位置,所以需要额外开辟出2*m个空间
将开辟出的空间链接到原字符串的后面,新的字符串命名为s_new设置两个指针p1和p2,初始时p1指向原字符串s的末尾,p2指向s_new的末尾
p1指针向前移动,当p1指向的字符不是空格时,将p1指向的字符复制到p2指向的位置,并都向前移动一位
当p1指向的字符是空格时,p1向前移动一格,这时应该插入%20,所以p2向前移动三格,并在这三格中插入%,2,0
时间复杂度O(n),空间复杂度O(n+2m)
'''
class Solution(object):

    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        space_count = 0
        for i in s:
            if i == ' ':
                space_count += 1
        s_len += 2 * space_count
        new_array = [' '] * s_len
        j = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_array[j] = '%'
                new_array[j+1] = '2'
                new_array[j+2] = '0'
                j += 3
            else:
                new_array[j] = s[i]
                j += 1
        return ''.join(new_array)
jie = Solution()
jie.replaceSpace('fuck you hahah penis')

'''
一趟遍历：
初始化一个空的字符串 res 并遍历输入字符串的每个字符 i：

如果 i 不是空格，直接加到 res 上；
如果是空格，则将结果加 %20。
'''
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i != ' ':
                res += i
            else:
                res += '%20'
        return res
jie = Solution()
jie.replaceSpace('fuck you hahah penis')

