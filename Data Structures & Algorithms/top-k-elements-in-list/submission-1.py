class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        tuplist = sorted(d.items(), key = lambda x: x[1], 
        reverse = True)
        firstx = tuplist[:k]
        out = []
        for item in firstx:
            out.append(item[0]) 
        return out

