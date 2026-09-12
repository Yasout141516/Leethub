class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=[set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        result=[]
        for letters in words:
            for row in rows:
                if all(char in row for char in letters.lower()):
                    result.append(letters)
                   
        return result