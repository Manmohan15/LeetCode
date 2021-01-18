def countVowelStrings(self, n: int) -> int:
        def count(n,c,dp):
            if dp[n][c]!=-1:
                return dp[n][c]
            if c<=0:
                return 0
            if n==1:
                return c
            dp[n][c]=count(n-1,c,dp)+count(n-1,c-1,dp)+count(n-1,c-2,dp)+count(n-1,c-3,dp)+count(n-1,c-4,dp)
            return dp[n][c]
        dp=[[-1]*51 for i in range(51)]
        return count(n,5,dp)
        
