# Main program
print("Welcome to the Financial Calculator!")
print("Please select an option:")
print("1. Percentage Calculator")
print("2. Loan Calculator")
print("3. Net Worth Calculator")
print("4. Retirement Savings Calculator")
print("5. Investment Portfolio Calculator")
print("6. Cash Flow Analysis")

# Get the user's choice
choice = int(input("Enter the option number: "))

# Perform the selected calculation
if choice == 1:
    print("Please select an option:")
    print("1. What is X% of Y?")
    print("2. What percentage is X of Y?")
    print("3. What percentage change from X to Y?")
    print("4. X is Y% of what number?")
    print("5. What's X with a change of Y%?")
    sub_choice = int(input("Enter the option number: "))
    if sub_choice == 1:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        result = x * y // 100
        print(f"{x}% of {y} is {result}")
    elif sub_choice == 2:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        result = x * 100 // y
        print(f"{x} is {result}% of {y}")
    elif sub_choice == 3:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        result = (y - x) * 100 // x
        print(f"The percentage change from {x} to {y} is {result}%")
    elif sub_choice == 4:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        result = x * 100 // y
        print(f"{x} is {result}% of what number?")
    elif sub_choice == 5:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        result = x * (100 + y) // 100
        print(f"{x} with a change of {y}% is {result}")
    else:
        print("Invalid option number")

elif choice == 2:
    loan_amount = int(input("Enter the loan amount: "))
    interest_rate = int(input("Enter the interest rate (in percentage): "))
    loan_term = int(input("Enter the loan term (in years): "))
    # Calculate the result of the formula
    monthly_rate = interest_rate // 12
    number_of_payments = loan_term * 12
    result = loan_amount * ((monthly_rate * (1 + monthly_rate) ** number_of_payments) // ((1 + monthly_rate) ** number_of_payments - 1))
    # Display the result to the user
    print(f"The monthly payment is {result}")

elif choice == 3:
    assets = int(input("Enter total assets: "))
    liabilities = int(input("Enter total liabilities: "))
    # Calculate net worth
    net_worth = assets - liabilities
    # Display the result to the user
    print(f"Net Worth: ${net_worth:,}")

if choice == 4:
    current_age = int(input("Enter current age: "))
    retirement_age = int(input("Enter retirement age: "))
    current_savings = int(input("Enter current retirement savings: "))
    annual_contribution = int(input("Enter annual contribution to retirement savings: "))
    expected_annual_return = int(input("Enter expected annual return (in percentage): "))
    # Calculate the result of the formula
    remaining_years = retirement_age - current_age
    total_savings = current_savings
    for i in range(remaining_years):
        total_savings = (total_savings + annual_contribution) * (1 + expected_annual_return / 100)
    # Display the result to the user
    print(f"Total retirement savings at age {retirement_age}: ${total_savings:,.2f}")

elif choice == 5:
    initial_investment = int(input("Enter initial investment amount: "))
    annual_return = int(input("Enter expected annual return (in percentage): "))
    investment_length = int(input("Enter investment length (in years): "))
    yearly_contribution = int(input("Enter yearly contribution amount: "))
    # Calculate the result of the formula
    total_investment = initial_investment
    for i in range(investment_length):
        total_investment = (total_investment + yearly_contribution) * (1 + annual_return / 100)
    # Display the result to the user
    print(f"Total investment after {investment_length} years: ${total_investment:,.2f}")

elif choice == 6:
    total_income = int(input("Enter total income: "))
    total_expenses = int(input("Enter total expenses: "))
    # Calculate the result of the formula
    cash_flow = total_income - total_expenses
    # Display the result to the user
    print(f"Total cash flow: ${cash_flow:,.2f}")

else:
    print("Invalid option number")