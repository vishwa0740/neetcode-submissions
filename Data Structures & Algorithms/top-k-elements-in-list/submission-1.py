class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for n in nums:
            a[n]=a.get(n,0)+1
        b=sorted(a,key=lambda i:a[i], reverse=True)
        return b[:k]


        