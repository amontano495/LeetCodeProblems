class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        zero_count = 0
        while( i < len(nums) - 1 ):
            if nums[i] == 0:
                nums.pop(i)
                i = 0
                zero_count+=1
            else:
                i+= 1
        for i in range(zero_count):
            nums.append(0)
        return nums