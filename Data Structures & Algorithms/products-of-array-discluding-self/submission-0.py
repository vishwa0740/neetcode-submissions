class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]
        for i in range(1,len(nums)):
            l.append(l[i-1]*nums[i-1])
        r=[1]
        for i in range(len(nums)-2,-1,-1):
            r.append(r[-1]*nums[i+1])
        r.reverse()
        result=[]
        for i in range(0,len(nums)):
            result.append(l[i]*r[i])
        return result
        