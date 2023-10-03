import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        if x < 0:
            return False
        elif x< 10:
            return True
        digits = int(math.log(x, 10)) + 1
        base = int(math.pow(10, digits // 2))
        left, right = divmod(x, base)
        left_digits = int(math.log(left, 10)) + 1

        for i in range(digits // 2):
            right, right_rem = divmod(right, 10)
            left_base = int(math.pow(10, left_digits-1-i))
            left_rem,left= divmod(left,left_base)
            if not (right_rem == left_rem):
                return False
        return True

test = Solution()
result = test.isPalindrome(9)
print('isPalindrome', result)