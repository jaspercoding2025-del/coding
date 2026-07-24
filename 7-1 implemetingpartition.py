mylist=[60,80,30,90,40,50,70]
biggerlist=[100,5,10,1,50]
negativelist=[-9,-6,-2,4,7]
emptylist=[]
duplist=[5,5,5,5,5,6]
mylist2=[60,80,30,90,40,50,60,70]
lowindex=0
highindex=0
def partition(mylist,lowindex,highindex):
  if len(mylist)==0:
    return(mylist)
  pivot=mylist[lowindex]
  swapper=0
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
  print(mylist)
print("mylist")
partition(mylist,0,6)
print("emptylist")
partition(emptylist,0,0)
print("negativelist")
partition(negativelist,0,4)
print("duplist")
partition(duplist,0,5)     
print("biggerlist")
partition(biggerlist,0,4)
print("mylist2")
partition(mylist2,0,7)
