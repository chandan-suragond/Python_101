# def longest_palindrome(s):
#     n = len(s)
#     if n <= 1:
#         return s

#     dp = [[False] * n for _ in range(n)]
#     start = 0
#     max_len = 1

#     # Single character substrings are palindromes
#     for i in range(n):
#         dp[i][i] = True

#     # Check for palindromes of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             start = i
#             max_len = 2

#     # Check for palindromes of length > 2
#     for length in range(3, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 start = i
#                 max_len = length

#     return s[start:start + max_len]

# # Example usage:
# # s1 = "babae"
# # print(longest_palindrome(s1))  # Output: "bab" (or "aba")

# s2 = "cbbd"
# print(longest_palindrome(s2))  # Output: "bb"


def longest_palindromic_substring(s):
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check odd-length palindromes centered at i
        palindrome_odd = expand_around_center(i, i)
        # Check even-length palindromes centered between i and i+1
        palindrome_even = expand_around_center(i, i + 1)

        # Update longest palindrome found
        longest = max(longest, palindrome_odd, palindrome_even, key=len)

    return longest

# Example usage:
s = "babad"
result = longest_palindromic_substring(s)
print(result)  # Output: "bab" or "aba"
