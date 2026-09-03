class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams, strs

        for s in strs:
            count = [0] * 26 # a ... z -> [0, 0, ..., 0]

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
            # tuple(count) because lists cannot serve as keys in python dictionaries
        return list(res.values())