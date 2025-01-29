def prompt(message):
    print(f'==> {message}')

def calculate_monthly_payment(amount, rate, months):
    return round(amount * (rate / (1 - (1 + rate)
                        ** (-months))), 2)

while True:
    prompt('Welcome to Mortgage / Car Loan Calculator Program!')
    while True:
        prompt('What is the loan amount in dollars ($)? ')
        loan_amount = float(input())
        if loan_amount > 0:
            break
        prompt('Please enter a valid amount above $0')
    while True:
        prompt('What is the annual percentage rate (APR)? ')
        annual_percentage_rate = float(input())

        if float(annual_percentage_rate) >=1:
            break
        prompt('Please enter a valid APR percentage (>= 0)')
    prompt('What is the loan duration in years? ')
    loan_duration_years = float(input())
    loan_duration_months = loan_duration_years * 12
    monthly_interest_rate = annual_percentage_rate / 100 / 12
    monthly_payment = calculate_monthly_payment(loan_amount,
                                                monthly_interest_rate,
                                                loan_duration_months)

    print(f'The monthly payment is: ${monthly_payment}')

    prompt('Do you want calculate monthly payment again? (y/n)')
    answer = input()

    if answer.lower() != 'y':
        break
