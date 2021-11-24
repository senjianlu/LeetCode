# Minimum Index Sum of Two Lists（两个列表的最小索引总和）

## 链接
[leetcode](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)  
[leetcode-cn](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/)  

## 解法
### 第一版
**思路：**  
1. 比较两个列表长度，取较短的进行遍历
2. 如果在另一个列表中有相同的值则记录这两个索引之和，并比较
3. 如果最小索引之和已经小于当前元素在较短列表中的索引，退出循环

**代码：**  
```python
class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        origin_list = list1
        target_list = list2
        result_list = []
        min_index = 2001
        if (len(list1) > len(list2)):
            origin_list = list2
            target_list = list1
        for i, char in enumerate(origin_list):
            if (char in target_list):
                index_sum = i + target_list.index(char)
                if (index_sum < min_index):
                    min_index = index_sum
                    result_list = [char]
                elif(index_sum == min_index):
                    result_list.append(char)
                if (min_index < i):
                    break
        return result_list
```
**结果：**  
Runtime: `220 ms`, faster than `36.80%` of Python3 online submissions for Minimum Index Sum of Two Lists.  
Memory Usage: `14.7 MB`, less than `68.12%` of Python3 online submissions for Minimum Index Sum of Two Lists.  

### 第二版
**思路：**  
1. 将 `list1` 转为字典（字符串为键，索引为值）
2. 遍历 `list2`，如果元素存在于字典中就计算，并比较
3. 如果最小索引之和已经小于当前元素在 `list2` 中的索引，退出循环

较第一版采用了字典优化速度。

**代码：**  
```python
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
```
**结果：**  
Runtime: `152 ms`, faster than `74.48%` of Python3 online submissions for Minimum Index Sum of Two Lists.  
Memory Usage: `14.8 MB`, less than `68.12%` of Python3 online submissions for Minimum Index Sum of Two Lists.  