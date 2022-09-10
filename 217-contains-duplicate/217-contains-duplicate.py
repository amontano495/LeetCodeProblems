class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount = {}
        for n in nums:
            if n not in numCount.keys():
                numCount[n] = 1
            else:
                return True
        return False