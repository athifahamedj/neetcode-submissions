class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = res = 0 
        prefixSums = {0: 1}
        for i in nums :
            curr += i
            diff = curr - k 
            res += prefixSums.get(diff, 0)
            prefixSums[curr] = 1 + prefixSums.get(curr, 0)
        return res
        # print(res)
