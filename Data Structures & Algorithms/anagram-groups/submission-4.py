class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            save[tuple(count)].append(word)
        return list(save.values())