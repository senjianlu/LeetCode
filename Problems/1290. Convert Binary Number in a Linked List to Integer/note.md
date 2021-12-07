# Convert Binary Number in a Linked List to Integer（二进制链表转整数）

## 链接
[leetcode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)  
[leetcode-cn](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/)  

## 解法
### 第一版
**思路：**  
拼接为二进制后转十进制。  
**代码：**  
```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num_2 = ""
        while head:
            num_2 += str(head.val)
            head = head.next
        return int(num_2, 2)
```
**结果：**  
Runtime: `31 ms`, faster than `68.01%` of Python3 online submissions for Convert Binary Number in a Linked List to Integer.  
Memory Usage: `14.2 MB`, less than `69.19%` of Python3 online submissions for Convert Binary Number in a Linked List to Integer.  