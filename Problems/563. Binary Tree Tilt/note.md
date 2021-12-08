# Binary Tree Tilt（二叉树的坡度）

## 链接
[leetcode](https://leetcode.com/problems/binary-tree-tilt/)  
[leetcode-cn](https://leetcode-cn.com/problems/binary-tree-tilt/)  

## 解法
### 第一版
**思路：**  
递归，计算节点左右子节点的总值、计算坡度并记录。  
**代码：**  
```python
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            if (not node):
                return 0
            else:
                nonlocal result
                l = dfs(node.left)
                r = dfs(node.right)
                result += abs(l-r)
                return node.val + l + r
        dfs(root)
        return result
```
**结果：**  
Runtime: `76 ms`, faster than `29.38%` of Python3 online submissions for Binary Tree Tilt.  
Memory Usage: `16.4 MB`, less than `24.41%` of Python3 online submissions for Binary Tree Tilt.  