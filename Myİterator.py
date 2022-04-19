class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start +=1
            return x
        else:
            raise StopIteration

a = MyNumbers(5,10)

for i in a:
    print(i)
