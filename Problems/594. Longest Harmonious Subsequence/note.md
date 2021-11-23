# Longest Harmonious Subsequence（最长和谐子序列）

## 链接
[leetcode](https://leetcode.com/problems/longest-harmonious-subsequence/)  
[leetcode-cn](https://leetcode-cn.com/problems/longest-harmonious-subsequence/)  

## 解法
### 第一版
**思路：**  
1. 遍历列表统计各元素出现次数汇总成字典
2. 记录最长和谐子序列长度为 0
3. 遍历字典的键，如果字典中还存在：`键 + 1` 的键就将值相加和当前最长长度做对比取大，否则跳过  

**代码：**  
```python
class Solution:
    def findLHS(self, nums) -> int:
        repeat_count_dict = {}
        for num in nums:
            if (num not in repeat_count_dict.keys()):
                repeat_count_dict[num] = 1
            else:
                repeat_count_dict[num] += 1
        max_len = 0
        for num in repeat_count_dict.keys():
            if ((num+1) in repeat_count_dict.keys()):
                _len = repeat_count_dict[num] + repeat_count_dict[num+1]
                if (_len > max_len):
                    max_len = _len
        return max_len
```
**结果：**  
Runtime: `312 ms`, faster than `63.00%` of Python3 online submissions for Longest Harmonious Subsequence.  
Memory Usage: `16.1 MB`, less than `18.85%` of Python3 online submissions for Longest Harmonious Subsequence.