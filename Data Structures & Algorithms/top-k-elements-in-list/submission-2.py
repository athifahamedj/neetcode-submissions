class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq counter
        freq= {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        # create a bucket
        bucket  = [[] for _ in range(len(nums)+1)]
        # populate the bucket
        for items, val in freq.items():
            bucket[val].append(items)
        # traverse the bucket in reverse
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for x in bucket[i]:
        # filter out only the top topKFrequent
                res.append(x)
                if len(res) == k:
                    return res 
            
            

 