class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag={}
        ran={}
        for i in magazine:
            mag[i]=1+mag.get(i,0)
        for j in ransomNote:
            if j not in mag:
                return False
            elif mag[j]<=0:
                return False
            mag[j]-=1
        print(mag)
      
        return True
       
    