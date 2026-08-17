#1544. Make The String Great

class Solution:
    def makeGood(self, s: str) -> str:
        char = []
        for ch in s:
            if not char:
                char.append(ch)
            else:
                if abs(ord(ch) - ord(char[-1])) == 32:
                    char.pop()
                else:
                    char.append(ch)
        return "".join(char)           
