import os
if __name__=='__main__':
    f=open("simditor.css","r")
    print(f.read(1),end="")
    f.close()
    class Sb:
        a=1
        b=2
        __c=0
        def __init__(self,a,b):
            self.a=a
            self.b=b
            self.__c+=1
        def wow(self):
            print(self.a,self.b)
        def __privatemt(self):
            print(123)

a=Sb(1,2)
a.wow()
a._Sb__privatemt()
b=Sb(3,4)
c=Sb(3,4)
print(c._Sb__c)
try:
    a=1
except Exception:
    print("SB")
finally:
    print("哈哈")
def test():
    a=0
    for i in range(1,10):
        a=yield i
        print(a)
a=test()

next(a)
a.send(123123)
a.send(345345)
next(a)