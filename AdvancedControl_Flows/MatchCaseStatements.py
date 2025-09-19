#Imagine a program that needs to react differently based on various user inputs. 
#Traditionally, you might rely on a series of if, else, and elif statements to handle these situations.
#Enter Match Case statement was Introduced in Python 3.10, 
#Match Case provides a more concise and elegant approach for handling multiple conditions. 
# It offers several advantages compared to traditional if/else chains:
#                              Improved Readability: Match Case statements present conditions and corresponding code blocks in a clear and well-structured format. 
#                              This enhances code maintainability and makes it easier for you and others to understand the logic flow.
#                              Explicit Matching: Match Case statements explicitly state the conditions being evaluated, 
#                              unlike if statements that can sometimes hide the logic within the condition itself. This improves code clarity.
#                              Exhaustiveness Checking (Optional):Python can optionally perform exhaustiveness checking for Match Case statements. 
#                              This ensures that all possible cases are handled, preventing potential runtime errors.


#BASIC SYNTAX OF MATCHCASE:
#  match expression:
#    case pattern1:
#            code_block_1
#    case pattern2:
#            code_block_2
#    ...
#    case pattern_n:
#            code_block_n
#    Optional: _ (wildcard) for default case

day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another workday...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":  # Match multiple values with pipe (|)
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")

#In this example, the day variable is matched against specific weekdays. 
#Each matching case executes its corresponding code block, printing a message based on the user’s input. 
#Notice how the | (pipe) operator allows matching against multiple values in a single case.
