class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        save = set(nums)
        longest = 0

        for i in save:
            if i-1 not in save:
                length = 0
                while i+length in save:
                    length += 1 
                longest = max(longest, length)
        return longest
                    