class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        inta = int(a, 2)
        intb = int(b, 2)

        # testing: print(f"Binary: {a}, {b}. Integer: {inta}, {intb}.")

        bint = bin(inta + intb)[2:]

        return bint

        