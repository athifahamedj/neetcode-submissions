class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello5#world
        res = ""
        for word in strs:
            res += str(len(word))+"#"+word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        # since we're not using i relative to j its not 2 pointer
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i: j])
            word = s[j+1:j+length+1]
            i = j+1+length

            res.append(word)
        return res

            
            
            

