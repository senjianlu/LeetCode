# String Compression（压缩字符串）

## 链接
[leetcode](https://leetcode.com/problems/string-compression/)  
[leetcode-cn](https://leetcode-cn.com/problems/string-compression/)  

## 解法
### 第一版
**思路：**  
1. 遍历列表统计连续出现的元素和其个数，并拼接为字符串
2. 遍历结束后循环字符串各元素重新赋值给传入的列表 `chars` 

*注：使用了额外的空间做统计。*

**代码：**
```python
class Solution:
    def compress(self, chars) -> int:
        last_char = chars[0]
        last_repeat_count = 1
        _chars_str = ""
        for char in chars[1:]:
            if (char == last_char):
                last_repeat_count += 1
            else:
                _chars_str = _chars_str + last_char
                if (last_repeat_count > 1):
                    _chars_str += str(last_repeat_count)
                last_char = char
                last_repeat_count = 1
        _chars_str = _chars_str + last_char
        if (last_repeat_count > 1):
            _chars_str += str(last_repeat_count)
        for i, char in enumerate(list(_chars_str)):
            chars[i] = char
        return len(_chars_str)
```
**结果：**  
Runtime: `56 ms`, faster than `86.95%` of Python3 online submissions for String Compression.  
Memory Usage: `14.4 MB`, less than `35.13%` of Python3 online submissions for String Compression.  

### 第二版
**思路：**  
遍历列表，与下一个元素做对比，不同则记录。  
*注：不使用额外的空间。*  
**代码：**  
```python
class Solution:
    def compress(self, chars) -> int:
        repeat_count = 1
        record_index = 0
        chars_len = len(chars)
        for i, char in enumerate(chars):
            if (i == (chars_len-1) or char != chars[i+1]):
                chars[record_index] = char
                record_index += 1
                if (repeat_count > 1):
                    for num in str(repeat_count):
                        chars[record_index] = num
                        record_index += 1
                        repeat_count = 1
            else:
                repeat_count += 1
        return record_index
```
**结果：**  
Runtime: `60 ms`, faster than `66.88%` of Python3 online submissions for String Compression.  
Memory Usage: `14.4 MB`, less than `35.13%` of Python3 online submissions for String Compression.  