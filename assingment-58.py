# Assignment 58 from class

from faker import Faker
fake = Faker()

def load_names():
    global names
    names = []
    for i in range(30):
        name = fake.first_name()
        names.append(name)
    # names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isabella', 'Jake', 'Kate', 'Liam', 'Molly', 'Noah', 'Olivia', 'Patrick', 'Quinn', 'Rachel', 'Sarah', 'Tom']

def show_options():
    print("""Assingment 58 has three tasks to run
          0. Load random list of names
          1. Output the length of each name
          2. Remove names only if greater than 5
          3. Remove only names containing 'n' or 'N'
          4. Remove remaining names using .pop() and while
          ----------------------------------------------------------------
          5. Show names as python list
          6. Show options again
          7. Quit
          """)




show_options()
load_names()


while True:
    answer = input('Which do you want to do (m for menu)? ')
    if answer == '0':
        load_names()
        print('Loading...')
        print(names)
    if answer == '1':
        for name in names:
            print(f'{name} is {len(name)} characters')
    if answer == '2':
        new_names = names
        for name in list(names):
            if len(name) > 5:
                print(f'{name} is {len(name)} characters, removing')
                new_names.remove(name)
        names = new_names
    if answer == '3':
        for name in names:
            if 'n' in name or 'N' in list(name):
                print(f"{name} contains the letter 'n' and was removed")
                names.remove(name)
    if answer == '4':
        while len(names) > 0:
            print(f'removing {names.pop()} from list using .pop()')
        print('This is what is left:')
        print(names)
    if answer == '5':
        print(names)
    if answer in ['6','m','M']:
        show_options()
    if answer in ['7','q','Q']:
        break

            
    