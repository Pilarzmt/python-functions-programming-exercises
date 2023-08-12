# Your code goes here:
def render_person(param):
    return param

def render_person(name, age, gender, birthdate, eye_color):
    person_info = f"{name} is a {age} years old {gender} born in {birthdate} with {eye_color} eyes"
    return person_info

green = eye_color
5/22/1983 = birthday
Bob = name
23 = age
male = gender

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))