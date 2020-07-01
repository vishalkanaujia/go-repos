'''
Given a 32-bit signed integer, reverse digits of an integer.

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        sign = 1
        if num < 0:
            sign = -1
            num = num * -1
        
        temp = num
        result = 0
        
        while temp > 0:
            digit = temp % 10
            result *= 10
            result += digit
            
            temp = temp // 10 # <<<<-------------

        if result > (2 ** 31 - 1):
            return 0
        
        return sign * result