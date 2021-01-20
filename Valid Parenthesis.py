class Solution:
    def isValid(self, s: str) -> bool:
        l=['(','{','[']
        d={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in l:
                stack.append(i)
            else:
                if(len(stack)==0 or stack[-1]!=d[i]):
                    return False
                else:
                    stack.pop(-1)
        if len(stack)!=0:
            return False
        return True
        
