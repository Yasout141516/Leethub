class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2=sorted(nums)
        hashset={}
        for idx,val in enumerate(nums2):
            if val not in hashset:
                hashset[val]=idx
        print(hashset)
        result=[]
        for i in nums:
            result.append(hashset[i])
        return result