import math 

# two calculation methods explained below
# the user must then select either bond or investment calculation option

investment_ = "investment - to calculate the amout of interest you'll earn on your investment"
print(investment_)

bond_ = "bond       - to calculate the amount you'll have to pay on a loan"
print(bond_)

choice = "Enter either 'investment' or 'bond' from the menu above to proceed: "
print(choice)

# I am using case.fold() function below so that the input above is not
# afected the caps of the choice
calculation_choice = input("Do you want to do an investment or bond calculation?: ")
print(calculation_choice.casefold())

# if, elif and else statement is used for user's choice of calculation 

if calculation_choice == "investment":
    deposit = float(input("What is the amount of money you will be depositing?: "))
    P = deposit 
# user to enter the interest rate (as percentage). Only the number of 
# the interest should be entered and not % sign
    interest_rate = float(input("Enter the interest rate. Only the number and not the percentage sign:"))
    r = interest_rate / 100 
    years = int(input("Enter the number of years you plan on investing: "))
    t = years 
# there are two interest types, simple and compound
# the user is requested to choose one.
    interest = input("Do you want simple or coumpound interest: ")
    print(interest.casefold())

    if interest =="simple":
        simple = P *(1 + r*t)
        print(f"Your total investment amount using simple interest is:", simple)
    else:
        interest =="compound"
        compound = P * math.pow((1+r),t)
        print(f"Your total investment amount using compount interest is:", compound)

# below is the interest rate formula both for simple and compound interest 
elif calculation_choice == "bond":
    present_value = "bond"
    present_value = int(input("Enter the present value of the house: "))
    P = present_value

    interest_rate = int(input("Enter your interest rate: "))
    interest_rate = ((interest_rate/100)/12)
    i = interest_rate

    months_to_pay = int(input("Enter the number of months you plan to repay the bond: "))
    n = months_to_pay 
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"You will have to repay", repayment, "each month.")
else:
    print("You have not entered a valid input, please check the options again.")
    
