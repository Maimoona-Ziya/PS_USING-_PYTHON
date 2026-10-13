#VOTING ELIGIBILITY CHECKER

# Asking user's age 
age = int(input(" Enter your age : "))

# Confirming citizenship status
citizenship = input ("Confirm your citizenship status(y/n): ")

# Eligible to vote only if both the conditions are true.
if age >= 18 and citizenship is "y" :
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")

