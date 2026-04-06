class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new= "".join(char for char in s if char.isalnum())
        s_new = s_new.lower()
        pointer1 = 0
        pointer2 = len(s_new) -1
        
        

        while pointer1 < pointer2:
            if s_new[pointer1] != s_new[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True


        