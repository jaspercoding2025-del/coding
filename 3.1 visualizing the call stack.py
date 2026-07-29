def x():
  print("hi")
  x()
def divider(number):
  print(number)
  if number<2:
    return
  number=number//2
  divider(number)
divider(10000000000)
def subtracter(num):
  print(num)
  if num==1 or num==0:
    return
  num=num-10
  subtracter(num)
subtracter(1000)
