while True:
    try:
        age = int(input("How old are you? "))
        if age > 18:
            print(f"You can drive at age {age}.")
            break
        else:
            print("Please enter a valid integer age.")
    except ValueError:
        print("You can't mix integers with strings in a comparison")

