def debug_log(func):
    def deco(*args, **kwargs):  # 被装饰函数实际是执行deco，所以在此将被装饰函数参数进行传递
        print("装饰器函数作用-----打印所有参数：" + str(args) + ' ' + str(kwargs))
        args_len, kwargs_len = func(*args,**kwargs)         # 将被装饰函数的返回值接收
        return args_len, kwargs_len     # 返回被装饰函数的返回值
    return deco
