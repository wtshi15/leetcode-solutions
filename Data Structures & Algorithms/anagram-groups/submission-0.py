class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            k = "".join(sorted(list(i)))
            s = d.get(k, [])
            s.append(i)
            d[k] = s

        return d.values()