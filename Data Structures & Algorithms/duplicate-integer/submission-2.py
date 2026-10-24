class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = set()
        for item in nums:
            if item in empty:
                return True
            else:
                empty.add(item)
        return False


       