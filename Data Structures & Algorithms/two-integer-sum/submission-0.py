class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i, item in enumerate(nums):
            diff = target - item
            if diff in save:
                return [save[diff], i]
            else:
                save[item] = i
            