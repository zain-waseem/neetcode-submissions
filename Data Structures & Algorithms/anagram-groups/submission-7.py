class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save = defaultdict(list)
        
        for word in strs:
            alpha = [0] * 26
            for letter in word:
                alpha[ord(letter) - ord("a")] += 1

            save[tuple(alpha)].append(word)
        return list(save.values())
                