# Maximum Product Subarray（乘积最大子数组）

## 链接
[leetcode](https://leetcode.com/problems/maximum-product-subarray/)  
[leetcode-cn](https://leetcode-cn.com/problems/maximum-product-subarray/)  

## 解法
### 第一版
**思路：**   
1. 用元素 `0` 分割原字符串得到众小串
2. 计算各小串的最大乘积并做比较后返回  
> 考虑到列表中的数字都是整数，因此只要子串需要在不包含 0 的情况下尽可能的长，且负数个数始终维持为偶数。 

**代码：**  
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def get_max(_nums):
            negative_num_indexes = [i for i in range(len(_nums)) if _nums[i] < 0]
            if (len(negative_num_indexes) == 1):
                if (negative_num_indexes[0] == 0):
                    _max = reduce(lambda a,b:a*b,_nums[1:]) if len(_nums) > 1 else _nums[negative_num_indexes[0]]
                elif(negative_num_indexes[0] == (len(_nums)-1)):
                    _max = reduce(lambda a,b:a*b,_nums[0:-1]) if len(_nums) > 1 else _nums[negative_num_indexes[0]]
                else:
                    _max = max(reduce(lambda a,b:a*b,_nums[negative_num_indexes[0]+1:]), reduce(lambda a,b:a*b,_nums[0:negative_num_indexes[0]]))
            else:
                _max = max(reduce(lambda a,b:a*b,_nums[negative_num_indexes[0]+1:]), reduce(lambda a,b:a*b,_nums[0:negative_num_indexes[-1]]))
            return _max

        _nums = []
        _max = max(nums)
        for i in range(len(nums)):
            if (nums[i] != 0):
                _nums.append(nums[i])
                if (i != (len(nums)-1)):
                    continue
            if (_nums):
                product = reduce(lambda a,b:a*b,_nums)
                if (product < 0):
                    product = get_max(_nums)
                _max = max(product, _max)
                _nums = []
        return _max
```
**结果：**  
Runtime: `52 ms`, faster than `86.10%` of Python3 online submissions for Maximum Product Subarray.  
Memory Usage: `14.6 MB`, less than `18.93%` of Python3 online submissions for Maximum Product Subarray.  