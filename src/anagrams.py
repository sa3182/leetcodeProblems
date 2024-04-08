class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        for ch in s:
            if ch in anagram:
                anagram[ch] = anagram[ch]+1
            else:
                anagram[ch] = 1

        for ch in t:
            if ch in anagram:
                anagram[ch] = anagram[ch]-1
            else:
                return False
        for i in anagram.values():
            if i!=0:
                return False
        return True