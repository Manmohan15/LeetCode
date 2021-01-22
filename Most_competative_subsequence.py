class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i in range(n):
            while len(stack)+(len(nums)-i) >k and len(stack)>0 and nums[i] < stack[-1]:
                stack.pop()
            stack.append(nums[i])

        return stack[:k]
  
