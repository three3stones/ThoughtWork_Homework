"""
2.4.1 
斐波那契数列（Fibonacci sequence），又称黄金分割数列,指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
请使用编写一个生成器，输入n, 输出为斐波那契数列的生成器。
"""

def fi_gen(num):
    a, b = 0, 1
    count = 0
    while count < num:
        yield b             # yield断点
        a, b = b, a+b
        count += 1

fi_gen1 = fi_gen(5)         # 创建一个生成器  
print('fi_gen1的类型为： %s ' % type(fi_gen1))        # <class 'generator'>

for i in range(5):
    print(next(fi_gen1), end='\t')
