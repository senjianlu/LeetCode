#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/1217. Minimum Cost to Move Chips to The Same Position/main.py
# @DATE: 2021/12/06 Mon
# @TIME: 10:36:02
#
# @DESCRIPTION: 1217


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def minCostToMoveChips(self, position) -> int:
        def get_2(_position):
            if (len(_position) == 0):
                return [0, 0]
            else:
                n = _position.pop()
                _list = get_2(_position)
                _list[n%2] += 1
                return _list
        _list = get_2(position)
        return min(_list[0], _list[1])



"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    _input = [1, 1000, 2]
    print("输入：{}".format(str(_input)))
    result = solution.minCostToMoveChips(_input)
    print("结果：{}".format(str(result)))