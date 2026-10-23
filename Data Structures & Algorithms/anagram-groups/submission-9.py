class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #[0,0,0,0,0,0]
        #(0,0,0,0) : [word, word] = output 
        save = defaultdict(list)
        for word in strs:
            char = [0] * 26
            for letter in word:
                char[ord(letter) - ord("a")] += 1
            save[tuple(char)].append(word) 
        return list(save.values())