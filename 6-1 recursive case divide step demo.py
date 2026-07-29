mylist=[5,7,2,9,3]
emptylist=[]
negativelist=[-4,-7,-9]
mixedlist=[5,8,-3,4,-2,-9]
def divide(mylist):
  print(mylist)
  #base case
  if len(mylist)==1:
    return
  if len(mylist)==0:
    return
  
  
  #recursive case
  middleindex=len(mylist)//2
  print(middleindex)
  left_half=mylist[:middleindex]
  right_half=mylist[middleindex:]
  divide(left_half)
  divide(right_half)
  
  
divide(mylist)
divide(emptylist)
divide(negativelist)
divide(mixedlist)
