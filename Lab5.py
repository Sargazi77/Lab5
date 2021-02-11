     
import lab5_database
def main():
    while True:
        print('1- add user \n 2- Search for a user \n 3- Delete a user \n 4- update \n 9- Quit')
        user_input = int(input())
        if user_input == 1:
            add_user()
        elif user_input == 2:
            search_user()
        elif user_input == 3:
            show_all()
        #elif user_input == 9:
            break
    else:
        print("Invalid Choice")
def add_user():
    print('Please enter the name of the user you want to add')
    name = input()
 
    while len(name) == 0:
        print("You have to enter something")
        name = input()
    print('Please enter the country of the user you want to add')  
    country = input()
    while len(country) == 0:
        print("You have to enter something")
        country = input()  
    print('Please enter the number of cathcehs of the user you want to add')
    catches = input()
    while len(catches) == 0:
        print("You have to enter something")
        catches = input()
 
    lab5_database.add_user_to_db(name,country,catches)
    main()
 
 
 
def show_all():
    display_all= lab5_database.show_All()
    for x in display_all:
        print(x)
    main()
 
def search_user():
    name = input("PLease enter a name you want to search for")
    find = lab5_database.search(name)  
    #
    print(find)     
    main()
if __name__== "__main__":
    main()
 