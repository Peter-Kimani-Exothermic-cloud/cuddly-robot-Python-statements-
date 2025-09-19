#Let’s build a program that calculates a discount on a purchase amount based on different purchase tiers:

purchase_amount = float(input("Enter your purchase amount:"))

if purchase_amount >= 1000:
    discount = 0.1 #10% discount

elif purchase_amount >= 500:
    discount = 0.05 #5% discount

else:
    discount = 0 # No discount

final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))

#This program takes the purchase amount as input. 
#It then uses a series of conditional statements: 
# * The first if statement checks if the purchase amount is greater than or equal to 1000:
#         If so, it applies a 10% discount. 
# * The elif statement checks if the amount is between 500 and 1000 (excluding 1000). 
#            If so, it applies a 5% discount. * If neither of the above conditions is met, the else block executes, and no discount is applied. 
# * Finally, the program calculates the final price by applying the discount and displays it to the user.