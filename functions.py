import random
import user_class


def getUniqueNumber():

    unique = False 
    while(not unique): 
        num = random.randrange(1,user_class.User.maxUsers)
           
        if(user_class.User.checkId_num(num) == True):
            unique = True   
    return num

def grabAge():
    
    while(True):
        age = input("Please enter a user's age:")
        if(len(age) > 0 and len(age) < 100 ):
            return age
        else:
            print("System catched an Error!/nIncorrect age format!\nEnter age between 1 to 100 ")

def grabHeight():
  while(True):
   height = int(input("Please enter a user's height in CM:"))
   if(height >= 1 and height <= 300 ): 
     return height
   else:
    print("System catched an Error!/nIncorrect Weight format!\nEnter Height between 1 to 300")


def grabWeight():
    while(True):
        weight = int(input("Please enter a user's weight in KG: "))
        if(weight >= 1 and weight <= 500 ):
            return weight
        else:
            print("System catched an Error!/nIncorrect Weight format!\nEnter Weight between 1 to 500 ")
def grabCompany():
    while(True):
        cpn = str(input("Please enter a user's Company he works: "))
        if(len(cpn) > 0 and len(cpn) < 100 ):
            return cpn
        else:
            print("Incorrect company format!\nEnter something... ")

def grabOccupation():
    while(True):
        occ = str(input("Please enter a user's work occupation: "))
        if(len(occ) > 0 and len(occ) < 100 ):
            return occ
        else:
            print("Incorrect work format!\nEnter sosmething... ")


def deleteUser():
    print("\nDeleting user...")
    selector = input("Please enter a name as identifier: ")

    user_class.User.delUser(selector) 

def num_there(s):
    return any(i.isdigit() for i in s)



def loadDatabase():
 
    user_class.User.loadUsers()
    
#save database to csv file
def save_database():
    print("\nSaving Database....\n")
    user_class.User.saveUsers()
    return 1



def determineState():

    save=input("\nWould you like to save the database before closing? [Y/N]\n")

    if( save.lower() == "y" ):
        print("\nSaving database and exiting....\n")
        save_database()
    else:
        print("\nQutting program without saving....\n")
        
    return 1

def display_home_message():

    print("\nWelcome to User Management System")
    s = input("""Would you like to __
          1 - See Current Users
          2 - Add User
          3 - Delete User
          4 - Save Database
          5 - Quit\n""")

    return s


