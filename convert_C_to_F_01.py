# FILE NAME - convert_C_to_F_01.py

# NAME: Nate Cancel    
# DATE: 02-28-2025
# BRIEF DESCRIPTION: convert temp using a formula

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience
   
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########

(C = float(input("Enter a temperature in Celsius: ")))

F = (C * 9/5) + 32

print(f' {C} degrees Celsius is {F} degrees Fahrenheit.')

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''

'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?
float can hold different values and can change


2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?
float is better for this scenario to handle the endless possiblities of input from the user.




'''
