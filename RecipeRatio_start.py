def get_servings():
    while True:
        try:
            original_servings = int(input("Enter the number of servings the recipe is originally for: "))
            desired_servings = int(input("Enter the number of servings you wish to make: "))
            return original_servings, desired_servings
        except ValueError:
            print("Error: Please enter valid numerical values for servings.")


original_servings, desired_servings = get_servings()
print("Original servings:", original_servings)
print("Desired servings:", desired_servings)
