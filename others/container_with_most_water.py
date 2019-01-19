# O(nlogn) solution
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        loc = list(range(n))
        self.mergeSort_with_index(height, loc)

        covered_loc = [False]*n
        right = n-1
        maxarea = 0
        for i in range(n):
            maxarea = max(maxarea, height[i]*max(right-loc[i],0))
            covered_loc[loc[i]] = True
            # update right
            if loc[i]==right:
                while right >= 0 and covered_loc[right]:
                    right = right - 1    
        
        covered_loc = [False]*n
        left = 0
        for i in range(n):
            maxarea = max(maxarea, height[i]*max(loc[i]-left, 0))
            covered_loc[loc[i]] = True
            # update left
            if loc[i]==left:
                while left<n and covered_loc[left]:
                    left = left + 1   
        return maxarea
        
    def mergeSort_with_index(self, arr, idx):
        if len(arr)>1:
            m = len(arr)//2
            l_arr = arr[:m]
            l_idx = idx[:m]
            r_arr = arr[m:]
            r_idx = idx[m:]

            # sort left and right arrays
            self.mergeSort_with_index(l_arr, l_idx)
            self.mergeSort_with_index(r_arr, r_idx)
            # merge left and right sorted arrrays
            
            i = j = k = 0
            while i<len(l_arr) and j<len(r_arr):
                if l_arr[i] < r_arr[j]:
                    arr[k] = l_arr[i]
                    idx[k] = l_idx[i]
                    i += 1
                else:
                    arr[k] = r_arr[j]
                    idx[k] = r_idx[j]
                    j += 1
                k += 1
                
            while i<len(l_arr):
                arr[k] = l_arr[i]
                idx[k] = l_idx[i]
                i +=1 
                k +=1 
            while j<len(r_arr):
                arr[k] = r_arr[j]
                idx[k] = r_idx[j]
                j +=1 
                k +=1
                
                
                    
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]        
ans = sol.maxArea(height)        
print(ans)        