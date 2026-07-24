mylist=[4,7,5]
emptylist=[]
duplist=[1,1,7,-3,5]
neglist=[-9,7,2]
def quickselect(mylist,lowindex,highindex,k):
  #input(lowindex)
  #input(highindex)
  #print(mylist)
  if (highindex-lowindex)<=0:
    return mylist
 
  swapper=partition(mylist,lowindex,highindex) 
  #print(swapper)
  if swapper==k:
    return(mylist[k])
  #print(mylist)
  
  elif k<swapper:
    return quickselect(mylist,lowindex,swapper,k) 
  elif k>swapper:
    return quickselect(mylist,swapper+1,highindex,k)
    
def partition(mylist,lowindex,highindex):
  if len(mylist)==0:
    return(mylist)
  pivot=mylist[lowindex]
  swapper=lowindex
  emptycup=0

  for i in range(lowindex,highindex+1):
    if mylist[i]<pivot:
      #swap
      swapper+=1
      emptycup=mylist[i]
      mylist[i]=mylist[swapper]
      mylist[swapper]=emptycup
      
  
    #swap piviot with swapper
  #swapper-=1
  emptycup=pivot
  mylist[lowindex]=mylist[swapper]
  mylist[swapper]=emptycup
  return swapper
#print(quickselect(mylist,0,2,1))
#print(mylist)
#print(quickselect(emptylist,0,0,3))
#print(emptylist)
#print(quickselect(duplist,0,4,0))
#print(duplist)
print(quickselect(neglist,0,2,0))
print(neglist)
