'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_symbols = []
        brackets = {'(':')', '{':'}', '[':']'}
        
        count = len(s)
        
        for index, symbol in enumerate(s):
            if symbol in brackets:
                open_symbols.append(symbol)
            else:
                if open_symbols: # check if list is empty
                    top_stack = open_symbols.pop()
                    if brackets[top_stack] != symbol:
                        return False
                else:
                    return False

        if len(open_symbols) != 0:
            return False
        
        return True