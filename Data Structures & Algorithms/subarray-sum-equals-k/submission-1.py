class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        res =0 
        curr = 0
        for i in nums:
            curr += i
            diff = curr - k
            res+= prefixSum.get(diff, 0)
            prefixSum[curr] = prefixSum.get(curr, 0) + 1
        return res
            
            