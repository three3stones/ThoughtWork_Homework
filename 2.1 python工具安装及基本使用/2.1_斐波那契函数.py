"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
请编写一个函数输入n, 输出n个斐波那契数列的列表。 如：fib(5) -> [1, 1, 2, 3, 5]
"""
def fibonacci_sequence(num):
    """
    @param num: 斐波那契数列的元素个数
    @return: 包含num个元素列表形式的斐波那契数列
    """
    result = []             # 存储最终结果列表
    a, b = 0, 1
    count = 1               # 记录数列的长度
    while count <= num:
        result.append(b)
        a, b = b, a + b
        count += 1
    return result

print(fibonacci_sequence(10))