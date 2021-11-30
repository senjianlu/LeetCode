# Decrypt String from Alphabet to Integer Mapping（解码字母到整数映射）

## 链接
[leetcode](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)  
[leetcode-cn](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)  

## 解法
### 第一版
**思路：**  
1. 使用 `"#"` 分割字符串，对长度大于 2 的子字符串进行二次分割，放入字符列表
2. 对字符列表最后一位进行判断，如果不为空说明原字符串不以 `"#"` 结尾，需要进行分割
3. 将字符列表各元素转为数字后 `+ 96 ` 后通过 `chr()`（ASCII 编码转为字符）方法转为字母
> ![ASCII 字符](https://raw.githubusercontent.com/senjianlu/imgs/master/20200213222741703.png)  

**代码：**  
```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars = []
        for _s in s.split("#"):
            while(len(_s) > 2):
                chars.append(_s[0])
                _s = _s[1:]
            chars.append(_s)
        if (chars[-1]):
            chars += list(chars.pop())
        else:
            chars.pop()
        return "".join([chr(int(char)+96) for char in chars])
```
**结果：**  
Runtime: `32 ms`, faster than `68.03%` of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.  
Memory Usage: `14.1 MB`, less than `94.47%` of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.  