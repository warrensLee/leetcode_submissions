class Solution:
    def reverse(self, x: int) -> int:


        string_x = str(abs(x))                  # make given integer a string
        string_x = string_x[::-1]               # reverse string
        string_x.lstrip('0')                    # remove leading 0
        
        if int(string_x) > 2147483648:          # if out of 2^31 bounds
            return 0
        if x < 0:                               # if negative before, adjust
            x = -1 * int(string_x)
        else:
            x = int(string_x)

        return x


        