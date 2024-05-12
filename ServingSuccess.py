
 # All 3 tasks
def adjust_recipe():
    try:
        
        original_servings = int(input("Enter the number of servings the recipe is originally for: "))
        desired_servings = int(input("Enter the number of servings you wish to make: "))

        
        adjustment_factor = desired_servings / original_servings

        
        print("Adjusted recipe quantities:")
        print(f"Original servings: {original_servings}")
        print(f"Desired servings: {desired_servings}")
        print(f"Adjustment factor: {adjustment_factor:.2f}")

    except ValueError:
        print("Error: Please enter valid numerical values for servings.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a nonzero value for original servings.")
    except ArithmeticError:
        print("Error: Arithmetic error occurred during calculation.")
    finally:
        print("Enjoy your cooking!")
 

adjust_recipe()
