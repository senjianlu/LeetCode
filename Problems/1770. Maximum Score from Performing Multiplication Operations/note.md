# Maximum Score from Performing Multiplication Operations（执行乘法运算的最大分数）

## 链接
[leetcode](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)  
[leetcode-cn](https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations/)  

## 解法
### 第一版
**思路：**  
递归并使用二维数组保存计算结果。

**代码：**  
```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        x2_list = [[None]*(m+1) for _ in range(m+1)]
        # l 为从左向右的指针索引，r 为从右向左的指针索引
        def get_max(l, r):
            if (x2_list[l][r] != None):
                return x2_list[l][r]
            if ((l+r) == m):
                return 0
            x2_list[l][r] = max(
                nums[l]*multipliers[l+r]+get_max(l+1, r),
                nums[-1-r]*multipliers[l+r]+get_max(l, r+1))
            return x2_list[l][r]
        return get_max(0, 0)
```
**结果：**  
Runtime: `8440 ms`, faster than `18.09%` of Python3 online submissions for Maximum Score from Performing Multiplication Operations.  
Memory Usage: `172.6 MB`, less than `6.38%` of Python3 online submissions for Maximum Score from Performing Multiplication Operations.  