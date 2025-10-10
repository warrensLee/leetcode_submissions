class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()               # remove initial whitespace

        if not s:
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]


        new = ""

        for i, num in enumerate(s):
            if num == 0:
                continue
            if num.isdigit():
                new += num
            else:
                break
        
        if new == "":
            return 0

        num = sign * int(new)
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num


        