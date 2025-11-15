#single inheriatnce
class parents:
  def function(self):
    print("i am good")
class child(parents):
  def function(self):
    print("i am bad")
obj=child()
obj.function()

obj=parents()
obj.function()
i am bad
i am good
