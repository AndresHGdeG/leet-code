class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last_number = 0
        total = 0
        for element in s:
            number = roman_dic[element]            
            if last_number < number :
                total += (number - 2*last_number)
            else:
                total += number
            last_number = number
        return total


test = Solution()
roman_number = 'MCMXCIV'
result = test.romanToInt(roman_number)
print(roman_number, "=", result)