from functools import reduce

class Solution(object):
    def find_shorter_string(self, a,b):
        return a if len(a) < len(b) else b

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        smallest_str = reduce(self.find_shorter_string, strs)
        last_ind = len(smallest_str)
        found = True
        while last_ind > 0:
            found = True
            for str in strs:
                if str[0:last_ind] != smallest_str[0:last_ind]:
                    found = False
                    break
            if found:
                break  
            else:        
                last_ind -= 1 
        return smallest_str[0:last_ind ]

print(Solution().longestCommonPrefix(['flower', 'flo', 'flight']))      