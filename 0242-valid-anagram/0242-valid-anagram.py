class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmaps={}
        hashmapt={}
        for number in range(len(s)):
            hashmaps[s[number]]=1+hashmaps.get(s[number],0)
            hashmapt[t[number]]=1+hashmapt.get(t[number],0)
        for count in hashmaps:
            if hashmaps[count]!=hashmapt.get(count,0):
                return False
        print(hashmaps)
        print(hashmapt)
        return True