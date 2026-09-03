class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s = {}
        seen_t = {}

        for char in s:
            if char not in seen_s:
                seen_s[char] = 1
            else:
                seen_s[char] += 1
        for char in t:
            if char not in seen_t:
                seen_t[char] = 1
            else:
                seen_t[char] += 1

        for char in seen_s:
            if (char not in seen_t) or (seen_s[char] != seen_t[char]):
                return False

        return True

