class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for item, val in freq.items():
            bucket[val].append(item)
        res = []
        for i in range(len(bucket) -1, -1, -1):
            for n in bucket[i]:
                res.append(n)
            
                if len(res) == k:
                    return res
        
            




        