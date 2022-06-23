class Solution:
    left = 0; right = 0
    maxLength = 0
    def find(self, start, end, s):
        while(start >= 0 and end < len(s) and s[start] == s[end]):
            if( (end - start + 1) > self.maxLength ):
                self.left = start
                self.right = end
                self.maxLength = end - start + 1

            start -= 1
            end += 1
    
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.find(i, i, s)
            self.find(i, i+1, s)
        
        return s[self.left:self.right+1]
    
   
        
        