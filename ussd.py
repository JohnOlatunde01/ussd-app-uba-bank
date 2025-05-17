ussd = input("Enter ussd code: ")


if ussd == "*919#": 
    print("welcome")
else:
    print("Invalid Ussd Code\n"
          "Try Again " 
          ) 
option = input (" 1. Buy Airtime\n2. Buy Data\n3. transfers\n4. Pay Bills\n5. Withdraw Cash\n6. Check Balance\n7. Exit\n\n")


print("You have selected option", option)
if option == "1":
 airtime_input = (" 1. airtime for self\n2. airtime for others\n3. back")
 if option == "1":
    pin= "1234" 
    print("please enter your four digital pin")
    if pin == ("correct pin"):
     print("You have sucessfully bought airtime")
else:
   print("invalid input")
if option == "2":
    data_input= ("1.data self\n2. data others")
    if option == "1":
     option_input = ("1. 100mb\n2. 200mb\n3. 500mb\n4. 1gig\n5. 5gig")
    if option == "1" "2" "3" "4" "5":
           print("you have sucessfully bought data")
    elif option == "2":
       print("input phone number")

if option == "3":
   account_number = input ("Enter account number")
   print("select recipient bank")
   recipient_bank = input ("1.Access bank\n2. wema bank\n3. GT bank\n4. first bank")
   if option == "1" "2" "3" "4":
     print("Transfer of {amount} to {recipient name} {account number} at {charge}")
     print("Please enter your four digits pin")
     len(pin) == 4 
     if len(pin) == 5:
      print ("incorrect pin")
     if len(pin) == 4:
        print("transaction sucessful")
        
if option == "4":
   Bills_input = ("1. cable/Tv\n2. Electricity-prepaid\n3. Electricity-postpaid\n4. Tolls")
   if option == "1" "2" "3" "4":
      print("input pin")
   if (pin) == ("1234"):
     print("transaction sucessful")
   else:
      print("invalid pin")

if option == "5":
   amount = input("Enter amount")
   balance = input("10000")
   if input == ("> 10000"):
    print(" insufficient funds")
else:
   print("Transfer Sucessful")

if option == "6":
   print("insert pin") 
   if pin == ("1234"):
    print("Enter amount")
   else:
      print("invalid pin") 

if option == "7":
   print("Bye")
   


    




      

   
   


    

   


   
   
    

   
   

    
   
    





               




    




     










