"""
任务描述：
商店里进行购物结算时会使用收银机（POS）系统，这台收银机会在结算时根据客户的购物车（Cart）中的商品（Item）进行结算和打印收据（Receipt）。
输入（样例）：
['ITEM000001','ITEM000001','ITEM000001','ITEM000001','ITEM000001',
'ITEM000003-2','ITEM000005','ITEM000005','ITEM000005']
其中对'ITEM000003-2'来说，"-"之前的是标准的条形码，"-"之后的是数量，数量会有为小数的可能性。
当我们购买需要称量的物品的时候，会由称量的机器生成此类标签（Tag），收银机负责识别生成收据。

任务要求：
使用python函数式的方式完成下列需求：
1. 对输入的列表进行合并汇总，对于样例输入输出如下：
    ITEM000001 5
    ITEM000003 2
    ITEM000005 3
2. 在需求1的基础上，写一个方法filterNumber(num)对数量进行过滤，过滤出大于num的商品及其数量，如：filterNumber(3, iter) => ITEM000001 5
"""

# 需求一
def result(items:list) -> dict:
    """
    @param items: 列表形式的收据清单
    @return: 返回字典形式的条形码及其对应的数量
    """
    res = dict()            # 使用字典来存储条形码及其对应的数量
    for item in items:
        if '-' in item:
            txm, num = item.split('-')
            if txm in res:
                res[txm] += int(num)
            else:
                res[txm] = int(num)
        else:
            if item in res:
                res[item] += 1
            else:
                res[item] = 1
    # 返回字典形式条形码以及数量
    return res

# 按要求输出合并汇总的结果
iter = ['ITEM000001','ITEM000001','ITEM000001','ITEM000001','ITEM000001',
'ITEM000003-2', 'ITEM000005', 'ITEM000005', 'ITEM000005']
for key, value in result(iter).items():
    print("条形码:%s  数量：%s" % (key, value))


# 需求二
def filterNumber(num:int, iter:list):
    """
    @param num: 定义过滤的数量
    @param iter: 列表形式的收据清单
    @return: 返回大于过滤数量的条形码以及数量
    """
    item_dict = result(iter)
    for key, value in item_dict.items():
        if value > num:
            print("条形码:%s  数量：%s" % (key, value))




iter = ['ITEM000001','ITEM000001','ITEM000001','ITEM000001','ITEM000001',
'ITEM000003-2', 'ITEM000005', 'ITEM000005', 'ITEM000005']
filterNumber(3,iter)
