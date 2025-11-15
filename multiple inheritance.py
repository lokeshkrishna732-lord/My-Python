#multiple inheritance
class A:
  def fun1(self):
    print("day1")
class B:
  def fun2(self):
    print("day2")
class C(A,B):
  def fun3(self):
    print("everything")
obj1=A()
obj2=B()
obj3=C()
obj1.fun1()
obj2.fun2()
obj3.fun3()
day1
day2
everything
