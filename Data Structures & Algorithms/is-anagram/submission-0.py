class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        saveS = {}
        saveT = {}
        if len(s) != len(t):
            return False
            
        for i in s:
            if i in saveS:
                saveS[i] += 1
            else:
                saveS[i] = 1
        for j in t:
            if j in saveT:
                saveT[j] +=1
            else:
                saveT[j] =1
        return saveT == saveS