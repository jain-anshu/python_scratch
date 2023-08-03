class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_list = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                my_list.append(ch)
            else:
                if len(my_list) == 0:
                    return False
                if my_list[-1] == '(' and ch == ')' or my_list[-1] == '{' and ch == '}' or my_list[-1] == '[' and ch == ']':   
                    my_list.pop()
                else:
                    return False

        return False if len(my_list) > 0 else True

vp = Solution()
str = "((({{}})))"
print(vp.isValid(str))