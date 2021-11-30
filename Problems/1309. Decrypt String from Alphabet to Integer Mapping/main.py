#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1309. Decrypt String from Alphabet to Integer Mapping/main.py
# @DATE: 2021/11/30 Tue
# @TIME: 13:19:35
#
# @DESCRIPTION: 1309


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars = []
        for _s in s.split("#"):
            while(len(_s) > 2):
                chars.append(_s[0])
                _s = _s[1:]
            chars.append(_s)
        if (chars[-1]):
            chars += list(chars.pop())
        else:
            chars.pop()
        return "".join([chr(int(char)+96) for char in chars])


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    print("输入：{}".format(str(_input)))
    result = solution.freqAlphabets(_input)
    print("结果：{}".format(str(result)))