class Solution:
    def splitWordsBySeparator(self, words, separator):
        res = []
        for string in words:
            word = ""
            for ch in string:
                if ch == separator:
                    if word != "":
                        res.append(word)
                        word = ""
                else: 
                    word += ch
            if word != "":        
                res.append(word)
        return res 

print(Solution().splitWordsBySeparator(["flower.funds", "flo.wr.", ".flight..."], "."))