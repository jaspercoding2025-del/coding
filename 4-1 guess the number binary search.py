import random
def randomer():
  randomnum=random.randint(1,100)
  guesscounter=0
  while True:
    guesscounter+=1
    guess=random.randint(1,100)
    if guess==randomnum:
      return(guesscounter)
randomer()
sum=0
max=0
min=9999
guesstracker={}
for i in range(100):
  
  guesses=randomer() 
  sum+=guesses
  if guesses>max:
    max=guesses
  if guesses<min:
    min=guesses
  if guesses not in guesstracker:
    guesstracker[guesses]=1
  else:
    guesstracker[guesses]+=1
print(guesstracker)
print(max)
print(min)
average=sum/100
print(average)



def doer():
  randomnum=random.randint(1,100)
  low=1
  high=100
  guesscounter=0
  while True:
    guesscounter+=1
    guess=(low+high)//2
    #print(guess)
    if randomnum>guess:
      low=guess+1
    if randomnum<guess:
      high=guess-1
    if randomnum==guess:
      #print("you win")
      break
  #print(guesscounter)
  return(guesscounter)
sum=0
max=0
min=9999
guesstracker={1:0,2:0,3:0,4:0,5:0,6:0,7:0}
for i in range(100):
  
  guesses=doer() 
  sum+=guesses
  if guesses>max:
    max=guesses
  if guesses<min:
    min=guesses
  guesstracker[guesses]+=1
print(guesstracker)
print(max)
print(min)
average=sum/100
print(average)


