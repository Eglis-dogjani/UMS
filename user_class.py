import functions
import random
import csv

class User:

    database = "UserDatabase.csv"
    requirePassword = True
    maxUsers = 1000 #not used
    usersList = []
    myData = []

    def __init__(self, name, id_num, age, height, weight, company, occupation):
        self.name = name
        self.id_num = int(id_num)
        self.age = age
        self.height = height
        self.weight = weight
        self.company = company
        self.occupation = occupation
        self.usersList.append(self)
        
    def showObjectProperties():
        print("\nCurrent Objects in class: ")
        print("-------------------------")
        for j in range(0,len(User.usersList)):
            print(User.usersList[j].name)
            print(User.usersList[j].id_num)
            print(User.usersList[j].age)
            print(User.usersList[j].height)
            print(User.usersList[j].weight)
            print(User.usersList[j].company)
            print(User.usersList[j].occupation, "\n")

    
    def checkId_num(newNumber):
        for k in range(0,len(User.usersList)):
            if(User.usersList[k].id_num == newNumber ):
                return False
        return True

    
    def showUsers():
        print("\nThere are currently", len(User.usersList), "users in the system....")
        for user in User.usersList:
            print("\n")
            print("User Name:          " + user.name)
           # print(user.id_num)
            print("User Age:           ", user.age)
            print("User Height:        ", user.height)
            print("User Weight:        ", user.weight)
            print("User Company:       " + user.company)
            print("User Job is:        " + user.occupation)
            print("\n")

   
    def addUser():

        

        newUser = User(input("please enter a name:"),(
                  functions.getUniqueNumber()), (
                    int(functions.grabAge())), (
                     int(functions.grabHeight())), (
                      int(functions.grabWeight())), (
                       str(functions.grabCompany())), (
                        str(functions.grabOccupation())), 
                         )


        
        print("\nNew user added...\n")


    
    def loadUsers():
      #  print("\n\n\nLoading users from database file: ", User.database)
      #  print("\n\n")
        
        myFile = open(User.database, 'r')        
        with myFile:
            data = list(csv.reader(myFile))

            for entry in data:

                newuser = User(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]) 
 
    def saveUsers():
        tosave = []
        for i in range(0, len(User.usersList)):
            data = [User.usersList[i].name,  
                        User.usersList[i].id_num,                         
                         User.usersList[i].age,
                          User.usersList[i].height,
                           User.usersList[i].weight,
                            User.usersList[i].company,
                             User.usersList[i].occupation,
                              ]
            tosave.append(data)
        print("\n\nData Converted.....\n\n")
        myFile = open(User.database, 'w', newline='')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(tosave)
        print("\nDatabase saved....\n")








   
    def nameCompare(selector, username):


        selector = selector.lower()
        username = username.lower()

     
        sel = selector[0:selector.find(" ")]
        sel=sel.replace(" ","")
        ector = selector[selector.find(" ")+1:]
        ector=ector.replace(" ","")

        
        if( selector == username):
            return True

        
        elif( (username.find( sel ) != -1) or (username.find( ector ) != -1) ):
            return True

        
        elif( (username.find( sel[:3] ) != -1) or (username.find( ector[:3] ) != -1) ):
             return True 


    def delUser(selector):
   
        matches=[]

        
        if(functions.num_there(selector) ):
            print("\nNumber Found!!\n\n")

    
        else:
            print("No Number!!\nname identifier")
            for k in range(0,len(User.usersList)):
                if( User.nameCompare( selector, User.usersList[k].name ) ): 
                    matches.append(k)



        if( len(matches) == 1 ):
            
            print("\nOne possible match found\n")
            print("\nMatch Name: \n",User.usersList[matches[0]].name,"\n")
            toRemove=input("\nWould you like to delete a user? [Y/N]\n")
            
                                    
            

            if( toRemove.lower() == "y" ):
                print("Deleting User...")
                User.usersList.remove(User.usersList[ matches[0] ])
                print("User is deleted")
                
            else:
                print("\nContinuing without deletion....")
            
 
        else:
            print("\nDo Nothing...")





    def showUserByPosition(position):
        print(User.usersList[position].name)
        print(User.usersList[position].id_num)
        print(User.usersList[position].age)
        print(User.usersList[position].height)
        print(User.usersList[position].weight)
        print(User.usersList[position].company)
        print(User.usersList[position].occupation)        



        
    def showUserPosition(self):
      
        return True
    def showName(identifier):
        print(User.usersList[identifier].name)
        

