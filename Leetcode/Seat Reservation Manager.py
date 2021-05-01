from sortedcontainers import SortedList
class SeatManager:

    def __init__(self, n: int):
        self.sl = SortedList()
        for i in range(1,n+1):
            self.sl.add(i)

    def reserve(self) -> int:
        x = self.sl[0]
        self.sl.remove(x)
        return x
        
    def unreserve(self, i: int) -> None:
        self.sl.add(i)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
