# Print FooBar Alternately（ 交替打印 FooBar）

## 链接
[leetcode](https://leetcode.com/problems/print-foobar-alternately/)  
[leetcode-cn](https://leetcode-cn.com/problems/print-foobar-alternately/)  

## 解法
### 第一版
**思路：**  
手动加锁 `lock`，在为 `True` 时打印 `foo`，否则打印 `bar`。  
**代码：**
```python
import time

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                time.sleep(0.0000001)
                if (self.lock):
                    break
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock = False


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            while True:
                time.sleep(0.0000001)
                if (not self.lock):
                    break
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock = True
```
**结果：**  
Runtime: `62 ms`, faster than `29.21%` of Python3 online submissions for Print FooBar Alternately.  
Memory Usage: `14.7 MB`, less than `75.00%` of Python3 online submissions for Print FooBar Alternately.  