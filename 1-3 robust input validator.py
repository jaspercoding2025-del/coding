while True: 
  try:  
    age=input("how old are you?")
    print(age)
    if int(age)>18 and int(age)<99:
      break
  except ValueError:
    print("age has to be in number form")
    
