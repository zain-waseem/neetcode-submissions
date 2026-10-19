class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        save = set()
        for i in nums:
            if i in save:
                return True
            save.add(i)
        return False