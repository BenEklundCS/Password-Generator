# Password Generator
# Benjamin Eklund

from password import *

def main():
  
  length = getInput()
  password = generatePassword(length)
  print(password)
  
main()