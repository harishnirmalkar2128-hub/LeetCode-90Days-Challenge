class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        if 0 <= p <= self.w - 1:
            return [p, 0]
        elif self.w <= p <= self.w + self.h - 2:
            return [self.w - 1, p - (self.w - 1)]
        elif self.w + self.h - 1 <= p <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (p - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (p - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        p = self.pos
        if not self.moved or (p > 0 and p <= self.w - 1):
            return "East"
        elif p > self.w - 1 and p <= self.w + self.h - 2:
            return "North"
        elif p > self.w + self.h - 2 and p <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()