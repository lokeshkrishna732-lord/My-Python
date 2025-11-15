#area of circle
class areaofcircle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*self.radius*self.radius
obj=areaofcircle(10)
obj.area()
314.0
