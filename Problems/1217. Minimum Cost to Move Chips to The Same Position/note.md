# 1217. Minimum Cost to Move Chips to The Same Position（玩筹码）

## 链接
[leetcode](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)  
[leetcode-cn](https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/)  

## 解法
### 第一版
**思路：**  
1. 将列表中索引相差 2 的元素合并，最后列表中只剩两个元素
2. 取较小的元素的值  

**代码：**  
```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        _list = [0, 0]
        for no in position:
            _list[no%2] += 1
        return min(_list[0], _list[1])
```
**结果：**  
Runtime: `32 ms`, faster than `72.22%` of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.  
Memory Usage: `14.3 MB`, less than `19.23%` of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.  

### 第二版
**思路：**  
递归。

**代码：**  
```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        def get_2(_position):
            if (len(_position) == 0):
                return [0, 0]
            else:
                n = _position.pop()
                _list = get_2(_position)
                _list[n%2] += 1
                return _list
        _list = get_2(position)
        return min(_list[0], _list[1])
```
**结果：**  
Runtime: `20 ms`, faster than `99.79%` of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
Memory Usage: `14.5 MB`, less than `19.23%` of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.