#Basic Python programs...

print("Hello, World !")

#Pseudocoode :
# PROBLEM : Given a person's age, tell them if they can vote or not. Write LOGIC first.
# Logic: 
# write the person's age
# if age is more than equal to 18:
#    print 'you can vote'
# else:
#    print 'you cannot vote'

age = 22
if age >= 18 :
    print("You can vote.")
else:
    print("You can not vote.")


#PSEUDOCODE for PROBLEM : Program that takes a temperature in celsius and tells the user whether 
# it's 'Freezing'(0 or below), 'Cold'(1-15), 'Mild'(16-25) or 'Hot'(above 25).
# Logic:
# temp = write/enter temperature in celsius.
# if temp <= 0:
#    print 'Freezing'
# else if temp >= 1 and temp <= 15:
#    print 'Cold'
# else if temp >= 16 and temp <= 25:
#    print 'Mild'
# else:
#    print 'Hot'   

temp = int(input("Enter temperature in celsius : "))
if temp <= 0:
   print('Freezing')
elif temp >= 1 and temp <= 15:
   print('Cold')
elif temp >= 16 and temp <= 25:
   print('Mild')
else:
   print('Hot')   

#PRACTICE PROBLEMS (PSEUDOCODE):
# Problem 1: Program for checking whether a number is even or odd.
# Logic: 
# num = write/enter a number.
# if num % 2 == 0(if number is divisible by 2):
#    print 'EVEN'
# else:
#    print 'ODD'

num = int(input("Enter a number: "))
if num % 2 == 0 :
   print('EVEN')
else:
   print('ODD')

# Problem 2: Program for finding the largest of 3 numbers.
# Logic:
# num1 = write/enter first number
# num2 = enter second number
# num3 = enter third number
# if num1 >= num2 and num1 >= num3:
#    print 'num1 is largest.'
# elif num2 >= num1 and num2 >= num3: 
#    print 'num2 is largest.'
# else:
#    print 'num3 is largest.'

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
if num1 >= num2 and num1 >= num3:
   print ('num1 is largest.')
elif num2 >= num1 and num2 >= num3: 
   print ('num2 is largest.')
else:
   print ('num3 is largest.')

# Problem 3: Program breaking down 'Plan a birthday party' into a numbered list of smaller sub-tasks.
# 1. Choose a date, venue and time for the party.
# 2. Set budget and make a list of guests to be invited.
# 3. Send invitations.
# 4. Buy and gather everything needed like decorative items, cake, candles and snacks. 
# 5. Decorate the place and keep everything ready before the guests arrive.


# Problem 4: Program for simple login check(Username and Password match).
# Logic:
# username = Enter the username 
# password = Enter password
# if username is "Maimoona" and password == "Maimoona@123" :
#     print 'Logged in successfully..'
# else :
#     print 'Wrong password. Try again!'

correct_username = "maimoona"
correct_password = "Maimoona@123" 
username = input("Enter the username : ").lower()
password = input("Enter the password : ")

if username == correct_username and password == correct_password :
    print('Logged in successfully..')
else :
    print('Wrong password. Try again!')
