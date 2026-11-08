class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            keys = "".join(sorted(word))
            if keys not in res:
                res[keys] = []
            res[keys].append(word)
        # print(res)
        return list(res.values())
            
        