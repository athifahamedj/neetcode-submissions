class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq= {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i in t:
            freq[i] = freq.get(i, 0) - 1
        
        for item, val in freq.items():
            if val != 0 :
                return False
        return True