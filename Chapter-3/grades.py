# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade.
# If the user enters a value out of range, 
# print a suitable error message and exit. 
# For the test, enter a score of 0.85. 

score = float(input("Enter Score: "))

if score > 1:
    print('Error')
    
elif score < 0:
    print('Error')

elif score >= 0.9:
    print('A')
    
elif score >= 0.8:
    print('B')
    
elif score >= 0.7:
    print('C')
    
elif score >= 0.6:
    print('D')
    
else:
    print('F')