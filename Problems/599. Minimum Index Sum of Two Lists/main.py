#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: /root/GitHub/LeetCode/Problems/599. Minimum Index Sum of Two Lists/main.py
# @DATE: 2021/11/24 Wed
# @TIME: 15:03:46
#
# @DESCRIPTION: 599


"""
@description: 主解法
-------
@param:
-------
@return:
"""
class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        list1_dict = {list1[i]:i for i in range(len(list1))}
        min_index = 2001
        result_list = []
        for i in range(len(list2)):
            if (list2[i] in list1_dict):
                index_sum = i + list1_dict[list2[i]]
                if (index_sum < min_index):
                    result_list = [list2[i]]
                    min_index = index_sum
                elif(index_sum == min_index):
                    result_list.append(list2[i])
            if (min_index < i):
                break
        return result_list


"""
@description: 单体测试
-------
@param:
-------
@return:
"""
if __name__ == "__main__":
    solution = Solution()
    list1 = ["k", "b", "c"]
    list2 = ["k", "b", "a"]
    print("输入：{}".format(str(list1)+str(list2)))
    result = solution.findRestaurant(list1, list2)
    print("结果：{}".format(str(result)))