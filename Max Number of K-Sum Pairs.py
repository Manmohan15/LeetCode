 def maxOperations(self, nums: List[int], k: int) -> int:
        d=collections.defaultdict(lambda:0)
        count=0
        for i in range(len(nums)):
          
            if d[k-nums[i]]!=0:
                count+=1
                d[k-nums[i]]= d[k-nums[i]]-1
            else:
                d[nums[i]]+=1
        return count        
        
