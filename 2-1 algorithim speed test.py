import random
import time
mylist=[]


def maximumfinder(book):
  currentmaximum=0
  for i in range (len(book)):
    if book[i]>currentmaximum:
      currentmaximum=book[i]
  print(currentmaximum)
#maximumfinder(mylist)


def orderer(car):
  duplicates=False
  for i in range (len(car)-1):
    for j in range (i+1,len(car)):
      #print (car[i])
      #print (car[j])
      if car[i]==car[j]:
        duplicates=True
  return duplicates
print(orderer(mylist))
paper=[]



#timing
start=time.time()
for i in range (1000000):
  paper.append(random.randint(1,1000))
end=time.time()
print(end-start)
start=time.time()
maximumfinder(paper)
end=time.time()
print("maxfinder:")
print(end-start)
'''
start=time.time()
orderer(paper)
end=time.time()
print("orderer:")
print(end-start)
'''
