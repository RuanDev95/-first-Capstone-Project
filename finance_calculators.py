# This is the Capstone Project I —Variables and Control Structures

import math

#Code to determin which calculation the user wants to do
calculator =input ('''
Choose either 'investment' or 'bond' from the menu belowe to proceed

investment        - to calculate the amount of interest you'll earn on interest 
bond                  - to calculate the amount you'll have to pay on a home loan \n ''') 

# Code thath will run if the user has entered 'investment'
if  calculator == "investment":
    calculator = True
    dep = float(input("Enter the amount you would like to deposit :\n "))
    interest_rate_input = int(input( "Enter the interesr rate ( no need to add the %) : \n"))
    years = int(input("The number of years you plan on investing for : \n"))
    interest = input("Do you want 'simple' or 'compound' interest :\n ")
    
#code that determin the interest that the user will recieve
#code thet will run once the user has entered simple 
    if interest == "simple":
        interest = True
        interest_rate = interest_rate_input / 100
        a =  dep *(1 +  interest_rate * years)
        print(" \n Your interest will be : " + str(a))
        
#code thet will run once the user has entered compound       
    if interest == "compound":
        interest = True
        interest_rate = interest_rate_input / 100
        a = dep * math.pow((interest_rate),  years )
        print(" \n Your interest will be : " + str(a))

# Code that will run if the user entered ' bond' 
if calculator =="bond":
 
    house_value = int(input("Enter the present value of the house : \n"))
    interest_rate_input= int(input("Enter the interest rate :\n"))
    interest_rate = (interest_rate_input/12)
    num_months = int(input("Enter the number of months to repay the bond :\n"))
    repayment = (interest_rate*house_value) / (1 - (1+ interest_rate)**(-num_months))
    print("\n Total of the amount that has to be paid each month : " + str(math.floor(repayment)))

    

   
    
    
          
    
    
    






