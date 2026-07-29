mylist=["6","4","1","5","3","2"]
emptylist=[]
negativelist=["-5","-9","3","_4"]
randomlist=["5","999","-1"]
sortedlist=["1","2","3","4","4"]

#sorts using bubble sort way. 
def bubsortfunction(mylist):
  for j in range(len(mylist)):
    for i in range(len(mylist)-1):
      if mylist[i]>mylist[i+1]:
        emptycup=0
        emptycup=mylist[i]
        mylist[i]=mylist[i+1]
        mylist[i+1]=emptycup
        
        
  return(mylist)
#checks if list is sorted
def checkersort(mylist):
  for i in range(len(mylist)-1):
    #print(mylist[i])
    if mylist[i]<mylist[i+1]:
      pass
      #print("true")
    if mylist[i]>mylist[i+1]:
      return False
  return True
      
print("test 1")
finalList=bubsortfunction(mylist)
if checkersort(finalList)==True:
  print("sorted")
else:
  print("notsorted")
  
  
print("test 2")
finalList=bubsortfunction(emptylist)
if checkersort(finalList)==True:
  print("sorted")
else:
  print("notsorted")
  
  
  
print("test 3")
finalList=bubsortfunction(negativelist)
if checkersort(finalList)==True:
  print("sorted")
else:
  print("notsorted")




print("test 4")
finalList=bubsortfunction(randomlist)
if checkersort(finalList)==True:
  print("sorted")
else:
  print("notsorted")



print("test 5")
finalList=bubsortfunction(sortedlist)
if checkersort(finalList)==True:
  print("sorted")
else:
  print("notsorted")
