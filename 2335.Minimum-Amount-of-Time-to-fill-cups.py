"""
You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

"""

class Solution:
    def fillCups(self, amount: list[int]) -> int:
        amount.sort()
        ans = 0
        while sum(amount) != 0:
            amount[2] -= 1
            if amount[1] != 0:
                amount[1] -= 1
            ans += 1
            amount.sort()
        return ans