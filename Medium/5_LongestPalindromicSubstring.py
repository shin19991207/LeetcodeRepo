class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        size = len(s)
        def _is_palindrome(s):
            return s == s[::-1]
        if _is_palindrome(s):
            return s
        for step in range(size):
            for curr in range(size):
                start, stop = curr, curr+step+1
                if stop > size:
                    break
                subs = s[start:stop]
                if _is_palindrome(subs) and len(subs) > len(palindrome):
                    palindrome = subs
        return palindrome
