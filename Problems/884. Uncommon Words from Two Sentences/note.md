# Uncommon Words from Two Sentences（两句话中的不常见单词）

## 链接
[leetcode](https://leetcode.com/problems/uncommon-words-from-two-sentences/)  
[leetcode-cn](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/)  

## 解法
### 第一版
**思路：**  
1. 使用空格分割后取差集
2. 差集中各单词在两个字符串中出现次数都小于等于 1 才取用  

**代码：**  
```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [w for w in list(set(s1.split(" "))^set(s2.split(" "))) \
            if (s1.split(" ").count(w) <= 1 and s2.split(" ").count(w) <= 1)]
```
**结果：**  
Runtime: `24 ms`, faster than `95.72%` of Python3 online submissions for Uncommon Words from Two Sentences.  
Memory Usage: `14.2 MB`, less than `83.63%` of Python3 online submissions for Uncommon Words from Two Sentences.  