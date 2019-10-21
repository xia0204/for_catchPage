
class Te_pro():
    def __init__(self):
        self.num = 20
    @property
    def ta(self):
        return self.num
    @ta.setter
    def ta(self,num):
        self.num=num
tt = Te_pro()
print(tt.ta)
tt.ta = 25
print(tt.ta)
