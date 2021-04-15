#多行输入输出的规范示例
'''
给出n阶方阵的所有数，求方阵里所有的数的和
输入：有多个测试用例，每个测试用例第一行为一个整数n（n《=1000）
接下啦是n行的数字，每行的数字，每行n个数用空格隔开。
输出：输入一个整数，表时n阶方阵的和
in：
3
1 2 3
2 1 3
3 2 1
out：
18
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)



# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
'''
求a+b的和
输入：
多组读入，每一行有两个数A，B。0《A，B《1000000
输出：
每行输出一个结果
in：
1 1
out：
2
'''
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))