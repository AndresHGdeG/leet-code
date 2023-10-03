import math
import queue

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        if x < 0:
            return False
        digits = int(math.log(x, 10)) + 1
        is_odd = self.isAnOddNumber(digits)
        middle = self.getMiddle(digits, is_odd)
        q_digits = queue.LifoQueue()
        for i in range(digits):
            x, residuo = divmod(x, 10)
            if i < middle:
                q_digits.put(residuo)
            else:
                if not (is_odd and i == middle):
                    compare = q_digits.get()
                    if not(compare == residuo):
                        return False
        return True

    def isAnOddNumber(self, n: int) -> bool:
        return not (n % 2) == 0

    def getMiddle(self, digits: int, is_odd : bool) -> int:
        if is_odd :
            return (digits - 1) // 2
        else:
            return digits // 2

test = Solution()
result = test.isPalindrome(12344321)
print('isPalindrome', result)