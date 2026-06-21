class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if no letter, if 1 letter base cases
        if len(s)<=1:
            return True

        #remove spaces
        #lowercase
        #remove punctuations

        new_s = ""
        for char in s:
            if char.isalnum():
                new_s+=char.lower()
        
        #use for loop to remove first and last letters
        for i in range(len(new_s)-1):
            print(f"first_char: {new_s[i]} and last_char: {new_s[len(new_s)-1-i]}")
            if new_s[i]==new_s[len(new_s)-1-i]:
                #new_s = new_s[i+1:len(new_s)-2]
                pass
            else:
                return False


        #if what remains is nothing or 1 char, then return true
        return True



