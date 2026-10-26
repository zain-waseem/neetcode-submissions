class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        save = set(nums1)
        save_two = set(nums2)

        for i in list(save):
            if i in save_two:
                save.remove(i)
                save_two.remove(i)

        return [list(save), list(save_two)]