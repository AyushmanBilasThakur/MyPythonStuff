# IN THIS PROBLEM WE NEED TO FIND THE POSITION IN WHICH A MAN CAN SURVIVE WHEN A PEOPLE IS KILLED AT THE SAME INTERVAL UNTIL ONLY ONE PEOPLE SURVIVES

array_of_people = []
no_of_people = int(input("No.of prople in initial circle: "))
interval = int(input("Special interval: "))
starting_index = int(input("Starting index: "))
a = 0
while(a<no_of_people):
    array_of_people.append(a)
    a += 1

array_of_people = array_of_people[starting_index - 1:] + array_of_people[:starting_index - 1]

while(len(array_of_people) > 1):
    eleminated = (interval % no_of_people) - 1
    del array_of_people[eleminated]
    array_of_people = array_of_people[eleminated:] + array_of_people[:eleminated]


print(array_of_people[0] + 1)