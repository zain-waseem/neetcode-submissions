class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save = {}
        for i in nums:
            save[i] = 1 + save.get(i,0)
           
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for key, value in save.items():
            freq[value].append(key)

        for i in range(len(freq) -1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

