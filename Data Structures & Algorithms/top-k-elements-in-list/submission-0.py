class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        sd = sorted(d.items(), key = lambda x: x[1], reverse = 1)
        lout = []
        for i in sd[:k]:
            lout.append(i[0])
        return lout

