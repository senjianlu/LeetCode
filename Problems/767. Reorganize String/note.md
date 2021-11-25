# Reorganize String（重构字符串）

## 链接
[leetcode](https://leetcode.com/problems/reorganize-string/)  
[leetcode-cn](https://leetcode-cn.com/problems/reorganize-string/)  

## 解法
### 第一版
**思路：**  
1. 计算各字符出现的次数，如果有超过总长度一半的直接返回空
2. 按出现次数倒叙
3. 构建长度为原字符串长度一半的两个列表（奇数长度会偏差 1），以较短的列表为基准，索引从后往前将较长列表的个元素插入

> ① 假设为出现次数：
> ```json
> {"a": 10, "b":8, "c": 3, "d": 1}
> ```
> `list1`: ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "b"]  
> `list2`: ["b", "b", "b", "b", "b", "b", "b", "c", "c", "c", "d"]  
> 受限于总出现次数大于总长度一半直接返回空，`list1` 中的 b 开头位置永远不会和 `list2` 中结尾的位置重合。  
> ② 而必须排序排序是因为：  
> `list1`: ["b", "b", "a"]  
> `list2`: ["a", "a"]  
> 类似上述情况会输出 `babaa`，不符合要求。

**代码：**  
```python
import math
import collections

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count_dict = collections.Counter(s)
        if (max(char_count_dict.values()) > math.ceil(len(s)/2)):
            return ""
        char_counts = char_count_dict.most_common()
        chars_str = "".join([str(char_count[0]*char_count[1]) \
            for char_count in char_counts])
        list1 = list(chars_str[0:math.ceil(len(s)/2)])
        list2 = list(chars_str[math.ceil(len(s)/2):])
        for i in range(len(list2), -1, -1):
            if (list1):
                list2.insert(i, list1.pop())
        return "".join(list2)
```
**结果：**  
Runtime: `28 ms`, faster than `92.31%` of Python3 online submissions for Reorganize String.  
Memory Usage: `14.1 MB`, less than `85.74%` of Python3 online submissions for Reorganize String.  