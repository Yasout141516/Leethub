class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashset={}
        for i in jewels:
            hashset[i]=0
        print(hashset)
        for j in stones:
            if j in hashset:
                hashset[j]+=1
        print(hashset)
        return sum(hashset.values())