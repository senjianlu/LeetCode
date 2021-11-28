# Reverse Words in a String（翻转字符串里的单词）

## 链接
[leetcode](https://leetcode.com/problems/reverse-words-in-a-string/)  
[leetcode-cn](https://leetcode-cn.com/problems/reverse-words-in-a-string/)  

## 解法
### 第一版
**思路：**  
使用 `.split()` 分隔字符串后倒叙拼接成结果。  
**代码：**  
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        _s = ""
        for word in s.split(" "):
            if (word):
                _s = word + " " + _s
        return _s.strip()
```
**结果：**  
Runtime: `28 ms`, faster than `93.47%` of Python3 online submissions for Reverse Words in a String.  
Memory Usage: `14.3 MB`, less than `87.73%` of Python3 online submissions for Reverse Words in a String.  