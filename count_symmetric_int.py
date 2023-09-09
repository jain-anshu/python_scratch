class Solution:
    def checksum(self, strnum, len):
        sum1 = 0
        sum2 = 0
   
        for i in range(0, int(len/2)):
            sum1 += int(strnum[i])
            sum2 += int(strnum[len - 1 - i])
        return sum1 == sum2    

    def countSymmetricIntegers(self, low, high):
        count = 0 
        for num in range(low, high + 1):
            strnum = str(num)
            if len(strnum) % 2 == 0:
                if self.checksum(strnum, len(strnum)):
                    count += 1
        return count

print(Solution().countSymmetricIntegers(1, 100))