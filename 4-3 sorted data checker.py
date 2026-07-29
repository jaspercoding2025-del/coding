datalist=["b","c","a"]
morelist=[]
moremorelist=["w","x","y","z"]
datawordlist=["pen","book","car"]
randomletterslist=["jis","qwer","yhfu"]
def checkersort(mylist):
  for i in range(len(mylist)-1):
    #print(mylist[i])
    if mylist[i]<mylist[i+1]:
      pass
      #print("true")
    if mylist[i]>mylist[i+1]:
      return False
  return True
print("---test 1---")
print(checkersort(datalist))
print("---test 2---")
print(checkersort(morelist))
print("---test 3---")
print(checkersort(moremorelist))
print("---test 4---")
print(checkersort(datawordlist))
print("---test 5---")
print(checkersort(randomletterslist))
