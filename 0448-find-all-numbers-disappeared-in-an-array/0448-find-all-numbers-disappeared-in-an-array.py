class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1=set(nums)
    
        missing=[]
        count=1
        for i in range(1,len(nums)+1):
            if i not in nums1:
                missing.append(i)
        return missing