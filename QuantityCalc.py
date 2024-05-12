def calculate_adjustment_factor():
    while True:
        try:
            original_servings = int(input("Enter the number of servings the recipe is originally for: "))
            desired_servings = int(input("Enter the number of servings you wish to make: "))
            adjustment_factor = desired_servings / original_servings
            return adjustment_factor
        except ValueError:
            print("Error: Please enter valid numerical values for servings.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please enter a nonzero value for original servings.")
        except ArithmeticError:
            print("Error: Arithmetic error occurred during calculation.")

# Example usage:
adjustment_factor = calculate_adjustment_factor()
if adjustment_factor is not None:
    print("Adjustment factor:", adjustment_factor)
