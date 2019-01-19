class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        
        # without converting to string
        n = self.num_digits(x)
        print('num digits', n)
        l = 10
        r = 10**(n-1)
        while l<=r:
            dr = x%l//(l//10)
            dl = x//r%10
            # print(l,r,' ',dl, dr)
            if dl == dr:
                l = l*10
                r = r//10
            else:
                return False
        return True
    
    def num_digits(self, x):
        # find number of digits in the integer
        if x==0:
            return 1
        n = 0
        while x!=0:
            x = x//10
            n += 1
        return n

sol = Solution()
x = 10
ans = sol.isPalindrome(x)
print(ans)