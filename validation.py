def get_valid_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value < 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter numerical digits.")