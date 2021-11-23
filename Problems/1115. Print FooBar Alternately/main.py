#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1115. Print FooBar Alternately/main.py
# @DATE: 2021/11/23 Tue
# @TIME: 14:26:36
#
# @DESCRIPTION: 1115


"""
@description: 打印 "foo"
-------
@param:
-------
@return:
"""
def printFoo():
    # print("foo")
    pass

"""
@description: 打印 "bar"
-------
@param:
-------
@return:
"""
def printBar():
    # print("bar")
    pass


import time

"""
@description: 主解法类
-------
@param:
-------
@return:
"""
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                time.sleep(0.0000001)
                if (self.lock):
                    break
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock = False


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                time.sleep(0.0000001)
                if (not self.lock):
                    break
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock = True


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":

    from threading import Thread

    _input = 1000
    print("输入：{}".format(str(_input)))
    start_time = time.time()
    foo_bar = FooBar(_input)
    threads = []
    threads.append(Thread(target=foo_bar.foo, args=(printFoo,)))
    threads.append(Thread(target=foo_bar.bar, args=(printBar,)))
    for thread in threads:
        thread.setDaemon(False)
        thread.start()
    for thread in threads:
        thread.join()
    print("耗时：{} 秒".format(time.time()-start_time))