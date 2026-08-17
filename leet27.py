#3813. Vowel-Consonant Score

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for ch in s:
            if ch == 'a' or ch == 'e' or ch =='i' or ch =='o' or ch =='u':
                v += 1
            elif ch.isalpha():
                c += 1
        if c == 0:
            return 0
        ans = int(floor(v/c))
        return ans
