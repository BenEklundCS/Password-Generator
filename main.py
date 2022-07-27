# Password Generator
# Benjamin Eklund

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

  chars = ['a','b','c','d','e',
           'f','g','h','i','j',
           'k','l','m','n','o',
           'p','q','r','s','t',
           'u','v','w','x','y',
           'z','!','@','#','$',
           '%','^','&','*']
  
  random.seed(time.time())
  roll = random.randrange(0,34)
  char = chars[roll]
  # add functionality to randomly uppercase letters 50% of the time
  return char
  
def generatePassword(length):
  password = []
  for i in range(int(length)):
    char = generateChar()
    password.append(char)
  str(password)
  result = (''.join(map(str, password)))
  return result
  
def main():
  
  length = getInput()
  password = generatePassword(length)
  print(password)
  
main()
