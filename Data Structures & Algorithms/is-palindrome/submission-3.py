class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Reduce s into alphannumeric
        #Remove space, ?
        new_list = ""
        for char in s:
            if char.isalnum():
                new_list+=char
        #Lowercase
        palindrome = new_list.lower()

        #check palindrome
        for i in range(len(palindrome)):
            if palindrome[i] != palindrome[-1-i]:
                return False
        return True
