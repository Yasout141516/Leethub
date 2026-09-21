class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        print(l,r)
        while l<r:
            summ=numbers[l]+numbers[r]
            if summ==target:
                return [l+1,r+1]
            elif summ<target:
                l+=1
            else:
                r-=1
        
            