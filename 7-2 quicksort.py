
mylist=[60,80,30,90,40,50,70]
biggerlist=[100,5,10,1,50]
negativelist=[-6,-9,4,-2,7]
emptylist=[]
smallerlist=[1,7,6,2]
duplist=[5,5,5,5,5,6]
mylist2=[60,80,30,90,40,50,60,70]
#lowindex=0
#highindex=0


def quicksort(mylist,lowindex,highindex):
  #input(lowindex)
  #input(highindex)
  #print(mylist)
  if (highindex-lowindex)<=0:
    return
 
  swapper=partition(mylist,lowindex,highindex) 
  #print(mylist)
  
  
  
  quicksort(mylist,lowindex,swapper)
  quicksort(mylist,swapper+1,highindex)
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
#quicksort(mylist,0,6)
#print(mylist)
#quicksort(smallerlist,0,3)
#print(smallerlist)
#quicksort(negativelist,0,4)
#print(negativelist)
#quicksort(biggerlist,0,4)
#print(biggerlist)
#quicksort(duplist,0,5)
#print(duplist)
#quicksort(emptylist,0,0)
#print(emptylist)
