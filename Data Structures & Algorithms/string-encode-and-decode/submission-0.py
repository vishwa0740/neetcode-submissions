class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for s in strs:
            a+=str(len(s))+"/"+s
        return(a)

    def decode(self, s: str) -> List[str]:
        e=[]
        i=0
        while i < len(s):
            j=i+1
            while s[j] != "/":
                j+=1
            c=int(s[i:j])
            k=j+1
            d=s[k:k+c]
            e.append(d)
            i=k+c
        return(e)
