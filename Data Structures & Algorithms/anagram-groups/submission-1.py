class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        outlist = []
        for word in strs:
            wordlist = list(word)
            wordlist.sort()
            wsorted = "".join(wordlist)
            d[wsorted].append(word)
        for item in d.values():
           outlist.append(item) 
        return outlist