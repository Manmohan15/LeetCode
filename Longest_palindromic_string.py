class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxcount=0
        maxstr=""
        for i in range(0,len(s)):
            count=0
            x=0
            while(i-x>=0 and i+x<len(s)):
                if(s[i-x]!=s[i+x]):
                    break
                x+=1
            count=2*(x-1)+1    
            if(count>maxcount):
                maxcount=count
                maxstr=s[i-x+1:i+x]
              
        for i in range(0,len(s)):
            count=0
            x=0
            while(i-x>=0 and i+x+1<len(s)):
            
                if(s[i-x]!=s[i+x+1]):
                    break
                x+=1
            count=2*x
            if(count>maxcount):
        
                maxcount=count
                maxstr=s[i-x+1:i+x+1]
        return maxstr        
                
