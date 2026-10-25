class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            keys = "".join(sorted(word))
            if keys not in seen :
                seen[keys] = []
            seen[keys].append(word)
        # print(seen)
        return list(seen.values())

