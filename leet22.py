#1046. Last Stone Weight


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) >= 2:
            stones.sort()

            lrg = stones.pop()
            slrg = stones.pop()

            if lrg != slrg:
                lrg = lrg - slrg
                stones.append(lrg)

        return stones[0] if stones else 0
