# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 
# and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - 
# you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function. 

def computepay(hour, rate):
    if hour < 40:
        return hour * rate
    
    else:
        return ((hour - 40) * 1.5 * rate) + 40 * rate

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))

pay = computepay(hrs, rate)
print("Pay", pay)