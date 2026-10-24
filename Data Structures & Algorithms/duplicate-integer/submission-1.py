class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)

        return len(sets) != len(nums)
        