# Jump Game III（跳跃游戏 III）

## 链接
[leetcode](https://leetcode.com/problems/jump-game-iii/)  
[leetcode-cn](https://leetcode-cn.com/problems/jump-game-iii/)  

## 解法
### 第一版
**思路：**  
从起点开始递归并记录走过的索引，出现重复或是索引到了列表外就返回 `False`，否则判断索引位置的值是否为 `0`。  
**代码：**  
```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        arrived = []
        def dfs(arr, i):
            if (i in arrived or i < 0 or i >= len(arr)):
                return False
            arrived.append(i)
            if (arr[i] == 0):
                return True
            return (dfs(arr, i+arr[i]) or dfs(arr, i-arr[i]))
        return dfs(arr, start)
```
**结果：**  
Runtime: `9804 ms`, faster than `5.02%` of Python3 online submissions for Jump Game III.  
Memory Usage: `74.7 MB`, less than `24.87%` of Python3 online submissions for Jump Game III.  