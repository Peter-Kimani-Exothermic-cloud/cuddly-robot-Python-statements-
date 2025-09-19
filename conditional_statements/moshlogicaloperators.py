

#Logical operators: and, or, not

#and
high_income = True
good_credit = True

if high_income and good_credit:
    print("Elgible")                   #Output is Elgible: Both conditions must be True

else:
    print("Not eligible")


#or
#atleast one of the arguemnts should be True

student = True
married = False

if student or married:
    print("Eligible")

else:                                  #Output is Eligible since one of the arguements was True
    print("Not eligible")  


 
             
             
            