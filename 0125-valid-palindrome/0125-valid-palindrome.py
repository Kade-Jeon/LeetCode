class Solution:
    def isPalindrome(self, s: str) -> bool:
        origin = list()
        temp1 = list()
        l = s.lower()
        
        for i in range(len(l)):
            if l[i].isalnum():
                origin.append(l[i])
                temp1.append(l[i])
        temp1.reverse()    
            
        return origin == temp1