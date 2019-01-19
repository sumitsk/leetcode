class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # works but slow
        # sum of elements and num_zeros after the current index
        # sumarr, nz = self.sum_arr(nums)
        # ans = self.recur(nums, 0, sumarr, nz, S)
        
        # using dynamic programming
        ans = self.dp(nums, S)
        return ans
    
    def dp(self, nums, target):
        # avoid consuming unnecessary space
        dp = {nums[0]: 1}
        self.add_to_dict(dp, -nums[0], 1)
        
        for i in range(1, len(nums)):
            new_dp = {}
            for k in dp:
                self.add_to_dict(new_dp, k-nums[i], dp[k])
                self.add_to_dict(new_dp, k+nums[i], dp[k])
            dp = new_dp                
        return (dp[target] if target in dp else 0)
    
    def add_to_dict(self, dct, key, val):
        if key in dct:
            dct[key] += val
        else:
            dct[key] = val

    def sum_arr(self, nums):
        ans = [nums[-1]]*len(nums)
        num_zeros = [1 if nums[-1]==0 else 0]*len(nums)
        i = len(nums)-2
        while i>=0:
            ans[i] = ans[i+1] + nums[i]
            num_zeros[i] = num_zeros[i+1] + (1 if nums[i]==0 else 0)
            i -= 1 
        return ans, num_zeros
    
    def recur(self, nums, i, sumarr, nz, target):
        if i==len(nums):
            return 0
        if sumarr[i]==target or sumarr[i]==-target:
            return 2**nz[i]
        elif sumarr[i]<target or -sumarr[i]>target:
            return 0

        return self.recur(nums, i+1, sumarr, nz, target-nums[i]) + self.recur(nums, i+1, sumarr, nz, target+nums[i])
                