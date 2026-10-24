class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            keys = "".join(sorted(word))
            if keys not in result :
                result[keys] = []
            result[keys].append(word)  
           
        
        return list(result.values())