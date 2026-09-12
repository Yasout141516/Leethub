class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon="balloon"
        ball={}
        
        count=0
        for i in text:
            if i in balloon:
                ball[i]=ball.get(i,0)+1
        return min(
            ball.get("b", 0),
            ball.get("a", 0),
            ball.get("l", 0) // 2,
            ball.get("o", 0) // 2,
            ball.get("n", 0)
        )
