class Solution:

    def encode(self, strs: List[str]) -> str:
        sout = ""
        for i in strs:
            li = len(i)
            sout+=str(li)+","+i
        return sout

    def decode(self, s: str) -> List[str]:
        lout = []
        markerindex = 0
        while 1:
            if markerindex >= len(s)-1:
                break
            commaindex = s[markerindex:].index(",")
            commaindex += markerindex
            lenstr = s[markerindex:commaindex]
            lenstr = int(lenstr)
            lout.append(s[commaindex+1:1+commaindex + lenstr])
            markerindex = commaindex + lenstr + 1
        return lout
# 1,a5,abcde3,abc
# 012345678901234
          # 1
# s.index(,) = 1
# lenstr = 1
# sout = 'a'
# markerindex = 1 + 1 = 2
