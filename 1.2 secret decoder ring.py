def encoder(message,shift):
  for i in range(len(message)):
    print(chr(ord(message[i])+shift))
    
encoder("hi",1)
def decoder(message,shift):
  for i in range (len(message)):
    print(chr(ord(message[i])-shift))
decoder("ij",1)
