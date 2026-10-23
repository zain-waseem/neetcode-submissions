class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        save_S = {}
        save_T = {}
        for i in s:
            if i in save_S:
                save_S[i] += 1
            else:
                save_S[i] = 1

        for i in t:
            if i in save_T:
                save_T[i] += 1
            else:
                save_T[i] = 1
        return save_S == save_T