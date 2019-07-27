"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        if len(num1) < len(num2):
            for i in range(len(num2) - len(num1)):
                num1.insert(0, "0")
        elif len(num1) > len(num2):
            for i in range(len(num1) - len(num2)):
                num2.insert(0, "0")

        result = 0
        for i in range(len(num1)):
            aver = (ord(num1.pop()) + ord(num2.pop())) % 48
            result += aver * 10 ** i
        return str(result)