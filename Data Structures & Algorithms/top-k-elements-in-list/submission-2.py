class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save = {}
        
        for i in nums:
            save[i] = 1+save.get(i,0)
        
        freq = [[] for i in range(len(nums)+1)]
        
        for key, value in save.items():
            freq[value].append(key)
        
        result = []
        for i in range(len(freq) -1,0,-1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result