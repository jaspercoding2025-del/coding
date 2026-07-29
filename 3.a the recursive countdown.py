def taker(num):
  print(num)
  if num==0:
    return("blast off")
  return taker(num-5)

print(taker(10))
