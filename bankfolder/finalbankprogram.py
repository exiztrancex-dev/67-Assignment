from bankfunctions import bank_account

didnt_quit = True
name = str(input("Please enter your name: "))  
customer1 = bank_account(name)

   
while didnt_quit == True:
    print("1. Make a deposit")
    print("2. Make a withdrawl")
    print("3. View account information")
    print("4. Quit")


    try:
        
       choice = int(input("Please choose an option: "))

       if choice == 1:
          deposit_amount = float(input("How much would you like to deposit?: "))
          customer1.make_deposit(deposit_amount)
       
       elif choice == 2:
          withdrawl_amount = float(input("How much would you like to withdraw?: "))
          if withdrawl_amount > customer1.total:
             print("Dont have enough money")
          else:
             customer1.make_withdrawl(withdrawl_amount)

       elif choice == 3:
          customer1.account_info(customer1.total, name, customer1.account_number )
       elif choice == 4:
          print("Thank you for your business")
          didnt_quit = False
    
       else:
          print("Invalid choice. Pick again")
          
    
    except ValueError:
       print("Invalid input please try again")
       