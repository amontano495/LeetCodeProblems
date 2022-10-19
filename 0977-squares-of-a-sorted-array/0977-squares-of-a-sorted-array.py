class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        ans = [0]*len(nums)
        k = len(ans) - 1
        while(i < j + 1):
            if nums[i] < 0:
                nums[i] = -1*nums[i]
            
            if nums[i] > nums[j]:
                ans[k] = nums[i] ** 2
                i += 1
                k -= 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
                k -= 1
        
        return ans
            