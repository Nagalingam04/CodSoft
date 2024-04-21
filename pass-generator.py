#importing modules
import string
import random

#password generating function
def password(length):

  alp_uc=string.ascii_uppercase
  alp_lc=string.ascii_lowercase
  digit=string.digits
  spe_ch=string.punctuation

  str=alp_uc+alp_lc+digit+spe_ch

  while True:
    pas_wd = ''
  
    for i in range(length):
      
      pas_wd+=random.choice(str)
      

    if any(char in spe_ch for char in pas_wd) and sum(num in digit for num in pas_wd)>=2:
      break 

  return pas_wd

#main function
def main():
  print("Enter the length of the password you want to generate: ")
  length=int(input())
  if length < 8:
    print("The password length should be greater than or equal to 8.\nRe enter password length:")
    length2=int(input())
    print("The Password is" , password(length2))
  else:
    print("The Password is" , password(length))
  
  
#main function calling
if __name__=="__main__":
  main()