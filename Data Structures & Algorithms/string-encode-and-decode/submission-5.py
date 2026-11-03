class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#words
        res = ""
        for word in strs:
            res+=str(len(word))+"#"+word
        return res

    def decode(self, s: str) -> List[str]:
        # 5#words
        # ["words"]
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            i = j+length+1
            res.append(word)
        return res



