class Fourcal:
    def __init__(self, first ,second):
        self.first =first
        self.second= second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a =Fourcal(4,2)
print(a.mul())

class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

a =MoreFourcal(4,3)
print(a.pow())    

class SafeFourcal(Fourcal):
    def div(self):
        if self.second ==0:
            return 0
        else :
            return self.first/ self.second



a= SafeFourcal(4,0)
print(a.div())        