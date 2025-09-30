class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # check if string is the same frontwards and backwards

        integer = str(x) # integer to string
        regetni = integer[::-1] # reverse string

        for i in range(len(integer)): # go thru each letter in string
            if (integer[i] != regetni[i]):  # if any letter doesnt match
                return False
        
        return True
        