import random, time

def getInput():
  # Add more choices like optional inclusion of special characters
  print("Enter desired password length: ")
  passwordLength = input()
  try:
    int(passwordLength)
    it_is = True
  except ValueError:
    it_is = False
    print('Input was not accepted - "ENTER AN INTEGER"')
    
  return passwordLength

def generateChar():
  # these will be used to add/remove special characters from password generation 
  min = 0
  max = 34
  #alpha = 26
  #special = 34

  # list of characters
  chars = ['a','b','c','d','e',
           'f','g','h','i','j',
           'k','l','m','n','o',
           'p','q','r','s','t',
           'u','v','w','x','y',
           'z','!','@','#','$',
           '%','^','&','*']
  # rolls a random number to choose characters
  random.seed(time.time())
  roll = random.randrange(min,max)
  char = chars[roll]
  # add functionality to randomly uppercase letters 50% of the time
  if char.isalpha():
    flip = random.randrange(2)
    if flip == 1:
      char = char.upper()
    else:
      pass
  else:
    pass
  # end of uppercase 50/50
  #returns generated character
  return char
  
def generatePassword(length):
  password = []
  for i in range(int(length)):
    char = generateChar()
    password.append(char)
  str(password)
  result = (''.join(map(str, password)))
  return result
    