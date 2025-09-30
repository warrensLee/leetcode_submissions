class Solution:
    def longestCommonPrefix(self, strs):
        # longest prefix in a string in an array of strings
        # compare each letter with one another if all elements of
        # the array have similar letters it is added to the prefix
        if not strs:
            return ""

        prefix = ""
        first = strs[0]

        for i in range(len(first)):                     # compare each letter in first word
            for s in strs[1:]:                          # compare each word to the first word
                if i >= len(s) or first[i] != s[i]:  
                    return prefix
            prefix += first[i]

        return prefix



