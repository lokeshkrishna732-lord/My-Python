#public and private modifiers
class encap:
  def __init__(self):
    self.mathan=100
    self.__rajesh=10
  def function(self):
    print(self.__rajesh)
obj=encap()
print(obj.mathan)
obj.function()
100
10
