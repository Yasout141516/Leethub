class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for index,number in enumerate(nums):
            if number!=index:
                return index
            elif index==len(nums)-1:
                return index+1
