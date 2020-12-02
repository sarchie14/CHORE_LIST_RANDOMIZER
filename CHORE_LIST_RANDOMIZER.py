#		 ALSO READ ON HOW TO SAVE THINGS TO A DOCUMENT.
# READ IN THE CHORE LIST FROM A DOC.
# Fix while statement in menu() where it will only accept y or n OR Y or N from user

menu = """***************************\n
		1. ENTER NEW CHORE\n
		2. REMOVE CHORE\n
		3. ENTER NEW MEMBER\n
		5. REMOVE MEMBER\n
		6. LIST CHORES\n
		7. LIST MEMBERS\n
		8. ASSIGN MEMBER'S CHORES\n
		9. SAVE INTO DOCUMENT\n
		***************************\n"""
chores = []

def new_chore(): 
    global chores
    i = 0
    
    print('Enter Chore -> ')
    newChore = input()

    chores = chores + [newChore]
    print('\nChore entered successfully')

def list_chores():
    global chores

    for x in chores:
        print(x)


def menu_selection(argument):
    if argument == '1':
        new_chore()
    elif argument == '6':
        list_chores()

def main():

    to_menu = True
    while to_menu:
        print(menu)

        user_menu_selection = input()
        menu_selection(user_menu_selection)

        print('Would you like to go back to menu?')
        
        user_input_to_menu = input()

        if user_input_to_menu != 'y':
            to_menu = False
main()    
