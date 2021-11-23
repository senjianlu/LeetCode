# Sign of the Product of an Array（数组元素积的符号）

## 链接
[leetcode](https://leetcode.com/problems/sign-of-the-product-of-an-array/)  
[leetcode-cn](https://leetcode-cn.com/problems/sign-of-the-product-of-an-array/)  

## 解法
### 第一版
**思路：**  
1. 遍历列表，出现 0 则直接返回，否则统计负数的个数
2. 负数个数为单数返回 -1，否则返回 1

**代码：**  
```python
class Solution:
    def arraySign(self, nums) -> int:
        negative_num_count = 0
        for num in nums:
            if (num == 0):
                return 0
            elif(num < 0):
                negative_num_count += 1
        if (negative_num_count%2 == 1):
            return -1
        else:
            return 1
```
**结果：**  
Runtime: `107 ms`, faster than `7.45%` of Python3 online submissions for Sign of the Product of an Array.  
Memory Usage: `14.1 MB`, less than `99.91%` of Python3 online submissions for Sign of the Product of an Array.  