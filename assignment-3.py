persons = [{'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'hiking']},
           {'name': 'Bob', 'age': 30, 'hobbies': ['tennis', 'cooking']},
           {'name': 'Charlie', 'age': 35, 'hobbies': ['guitar', 'traveling']}]

print(persons)

names = [person['name'] for person in persons]

are_all_persons_over_20 = all(person['age'] > 20 for person in persons)

persons_copy = [person.copy() for person in persons]
persons_copy[0]['name'] = 'Amy'

(Alice, Bob, Charlie) = persons
print(Alice)
print(Bob)
print(Charlie)

print(persons)
print(persons_copy) 