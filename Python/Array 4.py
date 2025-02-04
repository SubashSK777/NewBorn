class ProveSivarajIsWrongAndSubashIsRight:

  def __init__(self):
    self.a = 10
    self.b = 20

case1 = ProveSivarajIsWrongAndSubashIsRight()

case2 = case1


print(case1)
print(case2)

num1 = 9
num3  = num1

num3 = num3 - 7
print(id(num1) , id(num3))

