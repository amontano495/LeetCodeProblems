class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums) + 1):
            hashmap[i] = 1
        
        for num in nums:
            hashmap[num] -= 1
        
        for k,v in hashmap.items():
            if v == 1:
                return k