class Ece:

    company = 'anibaba'

    def userDinput(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = self.generateEmail(Ece)
    def generateEmail(self,cls):
        return f'{self.name}@{cls.company}.com'

    def appendInfo(self):
        with open('data.txt','a') as file:
            data = self.name+' '+self.age+' ' +self.gender+' ' +self.email+'\n'
            file.write(data)
    
    def deleteInfo(self):
        with open('data.txt','w') as file:
            data = "Name Age Gender Email\n"
            file.write(data)

    def showInfo(self):
       with open('data.txt','r') as file:
            data = file.read()
            print('\n'+data)
obj = Ece()    
def prompt(MenuInput):
    if MenuInput=='exit()':
        sure=input('Are You Sure!!(y/n) : ')
        if sure == 'y' or sure == 'Y':
            print('Thanks for using this app made by Aniket Raj Singh')
        elif sure == 'n' or sure =='N':
            print('\nThanks for you input, below is the Menu\n')
            menu()
        else:
            print('Please ENTER a Valid Command!!')
            MenuInput=input("To View Menu Press any key.\nTo Exit type exit()\n~")
            prompt(MenuInput)
    else:
        menu()

def addData(): 
    print("Please Enter Your Data Carefully\n")
    name=input("Please Enter Your Name : ")
    age=input("Please Enter Your Age : ")
    gender=input("Please Enter Your Gender : ")
    obj.userDinput(name,age,gender)
    obj.appendInfo()  
def menu():
    print('\nWelcome to the Student Data App \nPlease choose one of the options below.')
    print("1. Read Students Data")
    print("2. Add a Student's Data")
    print("3. Backup Students Data")
    print("4. Delete All Data")
    print("5. Exit the Menu")
    usrchoice = input("Please Enter 1 , 2 , 3 , 4 or 5 as your choice : ") 
    if usrchoice == '1':
        obj.showInfo()
        goback()
    elif usrchoice == '2':
        addData()
        goback()
    elif usrchoice == '3':
        print('Working on it')
        goback()
    elif usrchoice == '4':
        obj.deleteInfo()
        goback()
    elif usrchoice == '5':
        a = 'exit()'
        prompt(a)
        
def goback():
    gobk = input('Wanna go back to main menu?? (y/n) : ')
    if gobk == 'y' or gobk == 'Y':
        menu()
    elif gobk == 'n' or gobk == 'N':
        print('Thanks For Using This App')
        exit
    else:
        print('Please Enter Valid Input')   
            

        

        
