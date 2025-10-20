# ACME Bank Ltd. Mortgage Calculator
# Part 2: Monthly Payment Calculator with Amortization Schedule

# Constants for minimum down payment thresholds
PRICE_THRESHOLD_1 = 500000
PRICE_THRESHOLD_2 = 1000000

# Constants for down payment percentages
MIN_DOWN_PAYMENT_LOW = 5
MIN_DOWN_PAYMENT_MID = 10
MIN_DOWN_PAYMENT_HIGH = 20

# Constants for mortgage insurance rates
INSURANCE_RATE_1 = 4.0  # For down payment 5% to <10%
INSURANCE_RATE_2 = 3.1  # For down payment 10% to <15%
INSURANCE_RATE_3 = 2.8  # For down payment 15% to <20%
INSURANCE_RATE_4 = 0.0  # For down payment 20% and up

# Constants for mortgage terms and interest rates
TERM_1_YEAR = 1
TERM_2_YEAR = 2
TERM_3_YEAR = 3
TERM_5_YEAR = 5
TERM_10_YEAR = 10

RATE_1_YEAR = 5.95
RATE_2_YEAR = 5.9
RATE_3_YEAR = 5.6
RATE_5_YEAR = 5.29
RATE_10_YEAR = 6.0

# Constants for amortization periods
AMORT_5_YEAR = 5
AMORT_10_YEAR = 10
AMORT_15_YEAR = 15
AMORT_20_YEAR = 20
AMORT_25_YEAR = 25

# Get client information
client_name = input("Enter client name: ")
property_address = input("Enter address of property: ")
purchase_price = float(input("Enter purchase price: "))

# Calculate minimum down payment percentage based on purchase price
if purchase_price <= PRICE_THRESHOLD_1:
    min_down_payment_percent = MIN_DOWN_PAYMENT_LOW
elif purchase_price <= PRICE_THRESHOLD_2:
    # 5% on first $500,000 + 10% on remainder
    min_down_payment_amount = (PRICE_THRESHOLD_1 * MIN_DOWN_PAYMENT_LOW / 100) + \
                              ((purchase_price - PRICE_THRESHOLD_1) * MIN_DOWN_PAYMENT_MID / 100)
    min_down_payment_percent = round((min_down_payment_amount / purchase_price * 100), 3)
else:
    min_down_payment_percent = MIN_DOWN_PAYMENT_HIGH

# Get and validate down payment percentage
down_payment_percent = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent:.3f}): "))
while down_payment_percent < min_down_payment_percent or down_payment_percent > 100:
    print("Please enter a value between the minimum and 100")
    down_payment_percent = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent:.3f}): "))

# Calculate down payment amount
down_payment_amount = purchase_price * down_payment_percent / 100
print(f"Down payment amount is ${int(down_payment_amount)}")

# Determine mortgage insurance rate based on down payment percentage
if down_payment_percent < 10:
    insurance_rate = INSURANCE_RATE_1
elif down_payment_percent < 15:
    insurance_rate = INSURANCE_RATE_2
elif down_payment_percent < 20:
    insurance_rate = INSURANCE_RATE_3
else:
    insurance_rate = INSURANCE_RATE_4

# Calculate mortgage insurance cost
loan_amount = purchase_price - down_payment_amount
insurance_cost = loan_amount * insurance_rate / 100
print(f"Mortgage insurance price is ${int(insurance_cost)}")

# Calculate total mortgage (principal) amount
principal_amount = purchase_price - down_payment_amount + insurance_cost
print(f"Total mortgage amount is ${int(principal_amount)}")

# Get and validate mortgage term
mortgage_term = int(input(f"Enter mortgage term ({TERM_1_YEAR}, {TERM_2_YEAR}, {TERM_3_YEAR}, {TERM_5_YEAR}, {TERM_10_YEAR}): "))
while mortgage_term not in [TERM_1_YEAR, TERM_2_YEAR, TERM_3_YEAR, TERM_5_YEAR, TERM_10_YEAR]:
    print("Please enter a valid choice")
    mortgage_term = int(input(f"Enter mortgage term ({TERM_1_YEAR}, {TERM_2_YEAR}, {TERM_3_YEAR}, {TERM_5_YEAR}, {TERM_10_YEAR}): "))

# Get and validate amortization period
amortization_period = int(input(f"Enter mortgage amortization period ({AMORT_5_YEAR}, {AMORT_10_YEAR}, {AMORT_15_YEAR}, {AMORT_20_YEAR}, {AMORT_25_YEAR}): "))
while amortization_period not in [AMORT_5_YEAR, AMORT_10_YEAR, AMORT_15_YEAR, AMORT_20_YEAR, AMORT_25_YEAR]:
    print("Please enter a valid choice")
    amortization_period = int(input(f"Enter mortgage amortization period ({AMORT_5_YEAR}, {AMORT_10_YEAR}, {AMORT_15_YEAR}, {AMORT_20_YEAR}, {AMORT_25_YEAR}): "))

# Determine interest rate based on mortgage term
if mortgage_term == TERM_1_YEAR:
    annual_rate = RATE_1_YEAR
elif mortgage_term == TERM_2_YEAR:
    annual_rate = RATE_2_YEAR
elif mortgage_term == TERM_3_YEAR:
    annual_rate = RATE_3_YEAR
elif mortgage_term == TERM_5_YEAR:
    annual_rate = RATE_5_YEAR
else:  # TERM_10_YEAR
    annual_rate = RATE_10_YEAR

print(f"Interest rate for the term will be {annual_rate:.2f}%")

# Calculate effective monthly rate (EMR)
annual_rate_decimal = annual_rate / 100
effective_monthly_rate = ((1 + annual_rate_decimal / 2) ** 2) ** (1 / 12) - 1

# Calculate number of monthly payments
num_payments = amortization_period * 12

# Calculate monthly payment amount
monthly_payment = principal_amount * (effective_monthly_rate * (1 + effective_monthly_rate) ** num_payments) / \
                  ((1 + effective_monthly_rate) ** num_payments - 1)

print(f"Monthly payment amount is: ${int(monthly_payment)}")

# Ask if user wants to see amortization schedule
show_schedule = input("\nWould you like to see the amortization schedule? (Y/N): ")

if show_schedule.upper() == 'Y':
    print("                         Monthly Amortization Schedule")
    print(" ")
    print(f"{'Month':<5}    {'Opening Bal':>11}        {'Payment':>7}      {'Principal':>9}       {'Interest':>8}    {'Closing Bal':>11}")
    
    # Initialize variables for amortization schedule
    opening_balance = principal_amount
    total_principal = 0
    total_interest = 0
    
    # Calculate for each month of the term (not full amortization period)
    term_months = mortgage_term * 12
    
    for month in range(1, term_months + 1):
        # Calculate monthly interest
        monthly_interest = opening_balance * effective_monthly_rate
        
        # Calculate monthly principal
        monthly_principal = monthly_payment - monthly_interest
        
        # Calculate closing balance
        closing_balance = opening_balance - monthly_principal
        
        # Accumulate totals
        total_principal += monthly_principal
        total_interest += monthly_interest
        
        # Print the row
        print(f"{month:>5}     {opening_balance:>11.2f}       {monthly_payment:>7.2f}        {monthly_principal:>9.2f}        {monthly_interest:>8.2f}     {closing_balance:>11.2f}")
        
        # Update opening balance for next month
        opening_balance = closing_balance
    
    # Print separator and totals
    print("=" * 80)
    print(f"{'Total':<5}                                    {total_principal:>9.2f}      {total_interest:>8.2f}")