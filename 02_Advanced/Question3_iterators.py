class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step


    def __iter__(self):
        self.current = self.start
        return self
    # # wrong implementation
    # def __next__(self):
    #     if self.current >= self.stop:
    #         raise StopIteration

    #     current = self.current
    #     self.current += self.step
    #     return current

    # Tim solution
    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration

        self.current += self.step

        return self.current - self.step

r = Range(-2,-5,-1)

for x in r:
    print(x)