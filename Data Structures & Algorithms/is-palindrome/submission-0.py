class Solution:
    def isPalindrome(self, s: str) -> bool:
        # immediate case
        if (len(s) == 1):
            return True

        # lowercase string
        filtered = s.lower()

        # remove alphanumeric characters
        filtered = re.sub(r'[^a-zA-Z0-9]', '', filtered) # matches any character that isn't alphanumeric

        # with filtered string
        # -> traverse each character with two pointers
        front = 0
        back = len(filtered) - 1

        while front < back:
            if (filtered[front]  != filtered[back]):
                return False
            front += 1
            back -= 1
        
        return True