#step 1 check 
extracup=0
mylist=[3,5,7,2,9,4,7]
yourlist=[]
negativelist=[-5,-9,-79,5,2,4]
sortedlist=[1,2,3,4,5]
def insertion(mylist):
  for i in range(len(mylist)):
    print(mylist[i])
    for j in range(i,0,-1):
       if mylist[j]>=mylist[j-1]:
         break
       else:
         extracup=mylist[j]
         mylist[j]=mylist[j-1]
         mylist[j-1]=extracup
       print(mylist)
print("test 1: negative")
insertion(negativelist)
print("test 2:sortedlist")
insertion(sortedlist)
print("test 3: empty list")
insertion(yourlist)
print("test 4: OG list")
insertion(mylist)
