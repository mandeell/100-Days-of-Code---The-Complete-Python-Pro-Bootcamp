
# TODO-1: Ask the user for input
print('Welcome to the secret auction program.')
user_details = {}

while True:
    user_name = input('What is your name?: ')
    user_bid = int(input("What's your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
    user_details[user_name] = user_bid
# TODO-3: Whether if new bids need to be added
    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() != 'yes':
        break
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
if user_details:
    winner = max(user_details.items(), key=lambda x: x[1])
    print("\n" * 20)
    print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
else:
    print('No bids were placed.')
