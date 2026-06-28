class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        l=0
        for n in s:
            if n-1 not in s:
                len=1
                while (n+len) in s:
                    len+=1
                l=max(l, len)
        return l