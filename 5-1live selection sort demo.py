
def selsortorderer():
  mylist=[5,6,7]
  currentsmallestindex=0
  for j in range(len(mylist)):
    currentsmallest=mylist[j]
    currentsmallestindex=j
    for i in range(j,len(mylist)):
      mylist[i]
      if currentsmallest>mylist[i]:
        currentsmallest=mylist[i]
        currentsmallestindex=i
      #print(currentsmallest)  
    swapper=mylist[j]
    mylist[j]=mylist[currentsmallestindex]
    mylist[currentsmallestindex]=swapper
    #print(mylist)
  return(mylist)
print(selsortorderer())
