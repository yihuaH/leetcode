from distutils.command.install_lib import install_lib


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
            
class SmallestInfiniteSet:
    intlist = set()
    min_int = 0
    
    def __init__(self):
        for i in range(1000):
            self.intlist.add(i+1)
        
    def popSmallest(self) -> int:
        self.min_int = min(self.intlist)
        self.intlist.remove(self.min_int)
        return self.min_int

    def addBack(self, num: int) -> None:
        self.intlist.add(num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_',"") != target.replace('_',""):
            return False
        else: