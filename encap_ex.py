class Super:
    def __init__(self):
        self.v=50
        self._v1=100
        self.__v2=200
    def display(self):
        print(self.v)
        print(self._v1)
        print(self.__v2)
class Sub(Super):
    def show(self):
        print(self.v)
        print(self._v1)
        print(self.__v2)
# ob1=Sub()
# ob1.show()
ob1=Super()
ob1.display()
ob2 = Sub()
ob2.display()
ob2.show()