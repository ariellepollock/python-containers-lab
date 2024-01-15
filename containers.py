# Python Containers Lab

#####################################
# Exercise 1
#####################################
students = ['Milo', 'Avery', 'Eric', 'Devon']
print(students[1])
print(students[-1])


#####################################
# Exercise 2
#####################################
foods = ('olives', 'grapes', 'pretzels', 'walnuts')
for food in foods:
    print(f"{food} is a good food")


#####################################
# Exercise 3
#####################################
foods = ('olives', 'grapes', 'pretzels', 'walnuts')
last_foods = foods[-2:]
for food in last_foods:
    print(food)


#####################################
# Exercise 4
#####################################
home_town = {
    'city': 'Chicago',
    'state': 'Illinois',
    'population': '2.697 million'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


#####################################
# Exercise 5
#####################################
for key, value in home_town.items():
    print(f"{key} = {value}")


#####################################
# Exercise 6
#####################################
cohort = []
for idx, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[idx]
    })

for item in cohort:
    print(item)


#####################################
# Exercise 7
#####################################
awesome_students = [f"{student} is awesome!" for student in students]

for awesome_student in awesome_students:
    print(awesome_student)


#####################################
# Exercise 8
#####################################
a_in_foods = [food for food in foods if 'a' in food]

for food in a_in_foods:
    print(food)