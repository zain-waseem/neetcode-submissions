class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc,dec = True,True

        for i in range(len(nums)-1):
            if not nums[i+1] >= nums[i]:
                inc = False
            if not nums[i+1] <= nums[i]:
                dec = False
        return inc or dec