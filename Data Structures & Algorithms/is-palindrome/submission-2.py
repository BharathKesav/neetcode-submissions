class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for i in range(len(s)-1,-1,-1):
            if (ord(s[i])>=97 and ord(s[i])<=122) or (ord(s[i])>=65 and ord(s[i])<=90):
                rev=rev+s[i].lower()
            elif s[i].isdigit():
                rev=rev+s[i]
        new=rev[::-1]
        if rev==new:
            return True
        else:
            return False