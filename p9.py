#Scenario: You want to create a greeting system that can greet a single person or a group of people.

def greet_people(*people):
    if len(people) == 0:
        print("Hellow stranger!")
    elif len(people) == 1:
        print("Hello", people[0]+ "!")
    else:
        print("Hello", end="")
        for i in range(len(people)):
            if i == len(people)-1:
                print("and", people[i] + "!")
            else:
                print(people[i], end=",")

people = []
n= int(input("Enter no:of people:"))
print("Enter names:")
for i in range(n):
    name = input()
    people.append(name)
greet_people(*people)
