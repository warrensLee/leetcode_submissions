class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        last = {}
        start = 0

        # loop thru string, put all unique chars into dictionary 

        for i, char in enumerat(s):
            if char in last and last[carh] >= start:
                start = last[char] + 1                                # jump start past the duplicate
            last[char] = i
            longest = max(longest, i - start + 1)            
                
        print(longest)
        
        return longest
            
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}      # char -> last index
        start = 0      # start of current window
        best = 0

        for i, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] + 1       # jump start past the duplicate
            last[ch] = i
            best = max(best, i - start + 1)

        return best

        