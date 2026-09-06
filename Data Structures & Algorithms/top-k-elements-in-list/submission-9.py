class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        b=sorted(a,key=lambda c:a[c])
        return b[-k:]
        
