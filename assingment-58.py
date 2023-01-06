# Assignment 58 from class
# My current method for removing items is wrong, can't modify a list while iterating

def load_names():
    global names
    names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isabella', 'Jake', 'Kate', 'Liam', 'Molly', 'Noah', 'Olivia', 'Patrick', 'Quinn', 'Rachel', 'Sarah', 'Tom']

def show_options():
    print("""Assingment 58 has three tasks to run
          1. Load original list of names
          2. Output the length of each name
          3. Remove names only if greater than 5
          4. Remove only names containing 'n' or 'N'
          ----------------------------------------------------------------
          5. Show options again
          6. Show names as python list
          7. Quit
          """)




show_options()
load_names()


while True:
    answer = input('Which do you want to do? ')
    if answer == '1':
        load_names()
    if answer == '2':
        for name in names:
            print(f'{name} is {len(name)} characters')
    if answer == '3':
        new_names = names
        for name in names:
            if len(name) > 5:
                print(f'{name} is {len(name)} characters, removing')
                new_names.remove(name)
        names = new_names
    if answer == '4':
        for name in names:
            if 'n' in name or 'N' in name:
                print(f"{name} contains the letter 'n' and was removed")
                names.remove(name)
    if answer == '5':
        show_options()
    if answer == '6':
        print(names)
    if answer in ['7','q','Q']:
        break

            
    