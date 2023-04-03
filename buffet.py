# This program gives stock assesment based off many of the
# formulas used by the great Warren Buffet.

# Welcome the user to the program.
print()
print("Welcome to the Buffet Indicator. Follow the steps to find your values.")
print("I recommend using a platform like Yahoo Finance to find the values required.\n")

# Gross Margin.
print("First lets look at Gross Margin.")
print("This will require looking at the companies income statement.\n")
grossProfit = float(input("What was the companies Gross Profit for the last 12 months? "))
revenue = float(input("What was the companies Revenue for the last 12 months? "))
print()
answer = grossProfit/revenue * 100
print("A Gross Margin score consistently >40% is considered a good score.")
print(f"Gross Margin of this company is {answer:.2f}%")
print("A high Gross Margin shows the company isn't competing on price. It also shows the companies ability to pay expenses and shareholders.\n")

# Sales, General and Admin Expenses.
print("Now lets look at the companies Expenses score.")
print("This will require looking at the companies income statement.\n")
opEx = float(input("What was the companies Operating Expenses over the last 12 months? "))
print()
answer = opEx/grossProfit * 100
print("An Expenses score <30% is considered a good score. A score >80% is terrible.")
print(f"Expenses score of this company is {answer:.2f}%")
print("A good Expenses score displays a strong MOAT. Not needing to spend alot on overhead to operate.\n")

# Depreciation Expense.
print("Now we will calculate the Depreciation Expense.")
print("This will require looking at the companies cash flow statement.")
print("Depreciation is found under Operating Cash Flow, Cash Flow from COA.\n")
depreciation = float(input("What is the companies rate of Depreciation over the last 12 months? "))
print()
answer = depreciation/grossProfit * 100
print("A score of <10% is optimal.")
print(f"This company has a Depreciation score of {answer:.2f}%")
print("A good Depreciation score highlights that the company doesn't need a lot of capital expenditure assets to maintain its MOAT.\n")

# Interest Expense.
print("The next value is Interest Expense.")
print("This will require looking at the companies income statement.\n")
interestExpense = float(input("What was the companies Interest Expenses over the last 12 months? "))
operatingIncome = float(input("What was the companies Operating Income over the last 12 months? "))
print()
answer = interestExpense/operatingIncome * 100
print("A score <15% is considered good. A score >50% is considered bad.")
print(f"This companies Interest Expense score is {answer:.2f}%")
print("A good Interest Expense score shows the company doesn't need to rely on debt and spends a low amount of it's income on interest to service these debts.\n")

# Profit Margin or Net Margin.
print("Now lets look at the Profit Margin.")
print("This will require looking at the companies income statement.\n")
netIncome = float(input("What is the companies Net Income from Continuing and Discontinued Operations over the last 12 months? "))
print()
answer = netIncome/revenue * 100
print("A Profit Margin >20% is a good score. If <10% then reconsider.")
print(f"This companies Profit Margin score is {answer:.2f}%")
print("Companies that consistently convert >20% of their revenue into net income likely have a strong MOAT.")
print("However there is plenty of nuance between 10% and 20%\n")

# Debt to Asset Ratio
print("Lets look at the Debt to Asset Ratio.")
print("This will require looking at the companies balance sheet.\n")
debt = float(input("What is the companies Total Debt over the past 12 months? "))
assets = float(input("What are the companies Total Assets over the past 12 months? "))
print()
answer = debt/assets
print("A good score is anything <0.5. A bad score is anything >0.5.")
print(f"This companies Debt to Asset Ratio is {answer:.2f}")
print("A good Debt to Asset Ratio means that the company has more assets on its balance sheet than debt.\n")

# Capital Expenditures.
print("The next metric is Capital Expenditure.")
print("This will require looking at the companies cash flow statement.\n")
capitalExpenditure = float(input("What is the companies Capital Expenditure over the last 12 months?(Can be shown as a negative # but input as positive): "))
print()
answer = capitalExpenditure/netIncome * 100
print("A score <25% is optimal. A score >75% is not great.")
print(f"This company has a Capital Expenditure score of {answer:.2f}%")
print("Companies that have low Capital Expenditures have more money to reward shareholders. Note that this value can vary greatly over years so a 10 year average is best.\n")

# Total Liabilities to Shareholder Equity.
print("Now lets look at the Total Liabilities to Shareholder Equity ratio.")
print("This will require looking at the companies balance sheet.\n")
totalLiabilities = float(input("What are the companies Total Liabilities Net Minority Interest over the past 12 months? "))
shareholderEquity = float(input("What was the companies Common Stock Equity over the past 12 months? "))
treasuryShares = float(input("What is the Treasury Shares Number for the past 12 month period? (If none then 0): "))
print()
answer1 = shareholderEquity + treasuryShares
answer = totalLiabilities/answer1
print("A score <0.8 is a good score. A score >2 is not a good score.")
print(f"This company scores a {answer:.2f}.")
print("This shows a companies ability to finance itself with profits rather than debt.\n")

# Return on Shareholders' Equity.
print("Finally lets look at Return on Shareholder Equity.")
print("This can be calculated from previous input you have provided.\n")
answer = netIncome/answer1 * 100
print("A score >15% is a good score. A score <10% is not a good score.")
print(f"This company has a Return on Shareholders Equity of {answer:.2f}%")
print("This shows how effect management is at reinvesting their profits.\n")
print("That wraps up the Buffet Indicator program. Take note of the scores you received to compare across companies!\n")

