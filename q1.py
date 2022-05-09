# Write a program for ATM questions.
print("welcome to ATM machine:")
Name = input("please enter your name:  ")
print("welcome to Mr/Mrs.  " + Name)
language = input( "press 1 for 'English' or press 2 for 'Hindi' or press 3 for 'Tamil' or press 4 for 'Punjabi' :")
if language =='1':
 print("you choose : ", 'english')
elif language =='2':
 print("you choose : ", 'hindi')
 print("Thank you "+ Name,"to choose ")
elif language =='3':
  print("you choose : ", 'tamil')
  print("Thank you "+ Name, "to choose"+ 'Tamil')
elif language =='4':
  print("you choose :",'punjabi')
  print("Thank you "+ Name,"to choose "+ 'punjabi')
work=input("press 1 for 'check your balance' or press 2 for 'withdraw' or press 3 for 'entry of passbook':")
if work == 1:
  print("you check your balance")
  balance=300000
  print("your current balance is",balance)
elif work ==2:
    print("you choose:", 'withdraw your balance')
    a=int(input("enter you amount you want to withdraw:"))
    balance=300000
    if balance>=a:
        print("you have enough balance to withdraw:")
        pin=int(input("enter four digit pin number:"))
        if pin>=4:
            print("{} is your pin no.".fomat(a))
            print("you want receipt:")
            receipt=int(input("enter 7 to get receipt:"))
            print("you got your receipt")   
    else:
        print("you don't have enough balance:")       
elif work ==3:
    print("you choose:", 'entry your passbook')
    entry = int(input("press 8 to entry your passbook:"))
    print("your entry passbook is completed:")
print("Thank you to visit here, if you like it please visit again")


    
