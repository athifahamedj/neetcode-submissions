class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use bucket sort or heap method
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        for item, val in freq.items():
            bucket[val].append(item)
        res = []
        for x in range(len(bucket) - 1, 0, -1):

            for i in bucket[x] :
                res.append(i)
                if len(res) == k:
                    return res
                    # print(res)
            

        