class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fixed,l,r = nums[i],i+1,len(nums) - 1 
            while l < r :
                total = fixed + nums[l] + nums[r]
                if total > 0 :
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.append([nums[l], fixed, nums[r]])
                    r-=1
                    l+=1
                    # duplicates handling
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
        return res



         