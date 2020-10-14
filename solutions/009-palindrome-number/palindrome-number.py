# -*- coding:utf-8 -*-


# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Follow up: Could you solve it without converting the integer to a string?
#
#  
# Example 1:
#
#
# Input: x = 121
# Output: true
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Example 4:
#
#
# Input: x = -101
# Output: false
#
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            left = x
            right = 0
            while left > right:
                right = right*10 + left % 10
                left =left // 10
            return left == right or (left == right//10)
