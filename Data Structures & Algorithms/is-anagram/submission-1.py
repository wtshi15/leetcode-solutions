class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for letter in s:
            ds[letter] = ds.get(letter, 0) + 1
        
        for letter in t:
            dt[letter] = dt.get(letter, 0) + 1
        
        return ds == dt