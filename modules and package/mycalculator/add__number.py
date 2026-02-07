class Sum:
    def __init__(self,*num):
        self.num=num
    def add(self):
        return sum(self.num)