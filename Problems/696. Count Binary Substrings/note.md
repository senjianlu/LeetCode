# Count Binary Substrings（计数二进制子串）

## 链接
[leetcode](https://leetcode.com/problems/count-binary-substrings/)  
[leetcode-cn](https://leetcode-cn.com/problems/count-binary-substrings/)  

## 解法
### 第一版
**思路：**  
1. 遍历字符串，统计连续出现字符的个数
2. 两个相邻的连续字符个数取较小值

**代码：**  
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last_char = s[0]
        char_counts = [1]
        for char in s[1:]:
            if (char == last_char):
                char_counts[-1] += 1
            else:
                last_char = char
                char_counts.append(1)
        count = 0
        for i in range(1, len(char_counts)):
            count += min(char_counts[i-1], char_counts[i])
        return count
```
**结果：**  
Runtime: `156 ms`, faster than `84.95%` of Python3 online submissions for Count Binary Substrings.  
Memory Usage: `14.7 MB`, less than `13.43%` of Python3 online submissions for Count Binary Substrings.  