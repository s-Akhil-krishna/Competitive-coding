class MKAverage:

    def __init__(self, m: int, k: int):
        self.m , self.k = m,k
        self.sz = 0
        self.pq = []

    def addElement(self, num: int) -> None:
        self.pq.append(num)
        self.sz += 1

    def calculateMKAverage(self) -> int:
        m,k = self.m,self.k
        if self.sz <m:return -1
        container = self.pq[-m:]
        container.sort()
        i = k 
        j = m - k - 1
        if i > j:return 0
        sz = j - i + 1
        # print(container[i:j+1],sz,i,j)
        return sum(container[i:j+1])//sz
