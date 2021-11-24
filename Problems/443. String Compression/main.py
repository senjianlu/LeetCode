#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/443. String Compression/main.py
# @DATE: 2021/11/23 Tue
# @TIME: 17:34:13
#
# @DESCRIPTION: 443


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def compress(self, chars) -> int:
        repeat_count = 1
        record_index = 0
        for i in range(0, len(chars)):
            if (i == (len(chars)-1) or chars[i] != chars[i+1]):
                chars[record_index] = chars[i]
                record_index += 1
                if (repeat_count > 1):
                    for num in str(repeat_count):
                        chars[record_index] = num
                        record_index += 1
                        repeat_count = 1
            else:
                repeat_count += 1
        return record_index


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = ["a", "b", "b", "2", "2"]
    print("输入：{}".format(str(_input)))
    result = solution.compress(_input)
    print("结果：{}".format(str(result)))