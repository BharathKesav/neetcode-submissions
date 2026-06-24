class Solution:
    def isValid(self, s: str) -> bool:
        if s[0]=='}' or s[0]==']' or s[0]==')' or len(s)%2!=0:
            return False
        parent={'}':'{',']':'[',')':'('}
        ex= True
        stack=[]
        for i in s:
            if i=='{' or i=='(' or i=='[':
                stack.append(i)

            if len(stack)==0 and (i=='}' or i==']' or i==')') :
                ex=False
            elif i=='}' or i==']' or i==')':
                if parent[i]!=stack.pop():
                    ex=False
                
        if len(stack)!=0:
            ex=False
        return ex






        