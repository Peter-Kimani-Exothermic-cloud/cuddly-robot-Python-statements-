#Let us delve into building blocks that make control flow possible
#       if            This statement forms the foundation for decision-making.
#                     It evaluates a condition, and if the condition is True, the code block indented after the if statement is executed.
#       else
#       elif            



#Checking eligibility:

age = int(input("Enter your age"))

if age >= 18:
    print("You are eligibel to vote")

else:
    print("You are not eligible to vote")

#This program first takes the user’s age as input. 
#Then, the if statement checks if the age is greater than or equal to 18 (the voting age).
#If the condition is True, the program displays a message indicating eligibility
#If the condition is False (age less than 18), the else block executes, and the program displays a message stating ineligibility.