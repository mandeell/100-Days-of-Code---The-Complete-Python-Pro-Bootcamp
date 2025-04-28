import random

friends = []
number_of_people = int(input('How many people do you want to input: '))
for i in range(number_of_people):
    friend_name = input('Enter name: ')
    friends.append(friend_name)
print(random.choice(friends))


# "Alice", "Bob", "Charlie", "David", "Emanuel"
