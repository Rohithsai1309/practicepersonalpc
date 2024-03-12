class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindrome
            palindrome_odd = expand_around_center(i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd

            # Check for even-length palindrome
            palindrome_even = expand_around_center(i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even

        return longest
