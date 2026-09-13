class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=0
        maxCount=0
        hashset={}
        for i in nums:
            hashset[i]=hashset.get(i,0)+1
            result=i if hashset[i]>maxCount else result
            maxCount=max(hashset[i],maxCount)
        return result
        print(hashset)