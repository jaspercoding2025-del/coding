#lets person look for word
#get words from dictionary put into python list
book="dictionary.txt"
wordbank=[]
with open(book) as f:
  for word in f:
    word1=word.strip()
    wordbank.append(word1 )
#wordbank.pop(0)
#wordbank.pop(len(wordbank)-1)
print(wordbank)
#ask what word they want
#whatword=input("what word do you want?")

#searches and says if found
def junction(whatword,wordbank):
  for i in range(len(wordbank)):
    if wordbank[i]==whatword:
      print("word found page", i ,)
      return
  print("word not found")
#junction(whatword,wordbank)
def searcher(whatword,wordbank):
  
  #find middle word
  low=0
  high=len(wordbank)
  midpoint=(low+high)//2
  #before after or correct
  while True:
    print(low)
    print(high)
    print(midpoint)
    print(wordbank[midpoint])
    print(whatword)
    input()
    if wordbank[midpoint]==whatword:
      print("wordfound at" , midpoint , ".")
      return(midpoint)
    elif wordbank[midpoint]>whatword:
      high=midpoint
      midpoint=(low+high)//2
    elif wordbank[midpoint]<whatword:
      low=midpoint
      midpoint=(low+high)//2
#searcher(whatword,wordbank)


finallist=[]
def sorter(wordlist,n):
  print(wordlist)
  lettersinorder=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for i in range(26):
    lettersinorder[i]
    letterlist=[]
    for word in wordlist:
      if word[n]==lettersinorder[i]:
        letterlist.append(word)
    print(letterlist)
    #base case

    if len(letterlist)==0 or len(letterlist)==1:
      print(letterlist)
      finallist.append(letterlist)
      return(letterlist)
    #recursive case
    (sorter(letterlist,n+1))
print(sorter(wordbank,0))
print(finallist)

    
  
  
