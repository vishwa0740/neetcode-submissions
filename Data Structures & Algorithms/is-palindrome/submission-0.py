class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl=""
        for c in s:
            if c.isalnum():
                cl+=c.lower()
        l=0
        r=len(cl)-1
        while l<r:
            if cl[l]!=cl[r]:
                return False 
            l+=1
            r-=1
        return True