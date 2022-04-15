class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum()).lower()  # remove non char and set it to lower case
        index = len(s) - 1
        for c in s:
            if c != s[index]:
                return False
            index -= 1

        return True