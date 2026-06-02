class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        for i in s:
            a[i]=a.get(i,0)+1
        for i in t:
            a[i]=a.get(i,0)-1
        for b in a:
            if a[b]!=0:
                return False
        return True