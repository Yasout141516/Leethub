class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelmap={}
        for i in jewels:
            jewelmap[i]=0
        for j in stones:
            #print(j)
            if j in jewelmap:
                jewelmap[j]+=1
        return sum(jewelmap.values())