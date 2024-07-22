import sys
import user_class
import functions


functions.loadDatabase()



while( True ):

    s=functions.display_home_message()

    print("**The value chosen is: ",s)
    if(s == "1"):
        user_class.User.showUsers()    
    elif(s == "2"):
        user_class.User.addUser()
    elif(s == "3"):
        functions.deleteUser()  
    elif(s == "4"):
        functions.save_database()      
    #Savw changes made to DB
    elif(s == "5"):
        print("Quitting Program....")
       
        functions.determineState()
        sys.exit(0)
    else:
        print("Please enter a valid key...")
    print("\n\n")


