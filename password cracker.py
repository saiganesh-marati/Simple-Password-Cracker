from random import *
import os
user_passwd=(input("enter the password:"))
passwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
passwd1=['a','b','c','d','e','f','g','h','i','0','1','2','3']
pw=""
while(pw!=user_passwd):
    pw=""
    for letter in range(len(user_passwd)):
        guess_pwd=passwd1[randint(0,12)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("cracking password.... please wait!")
        os.system("cls")
print("password entered is :",user_passwd)
print("Your password is:",pw)

