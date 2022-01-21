import math, argparse

parser = argparse.ArgumentParser(description="This program is a loan calculator.")
parser.add_argument("--type", choices=["annuity", "diff"], help="You need to choose which type of loan you want to calculate.")
parser.add_argument("--principal", type=int, help="Enter the principal.")
parser.add_argument("--payment", type=float, help="Enter the payment.")
parser.add_argument("--interest", type=float, help="Enter the loan interest.")
parser.add_argument("--periods", type=int, help="Enter the number of periods.")
args = parser.parse_args()

params = []

loan_principle = args.principal
num_of_periods = args.periods
loan_interest = args.interest
monthly_payment = args.payment

if args.payment != None:
    params.append(monthly_payment)
if args.principal != None:
    params.append(loan_principle)
if args.periods != None:
    params.append(num_of_periods)
if args.interest != None:
    params.append(loan_interest)

length_list = len(params)

def calculate():
    global loan_interest, loan_principle, num_of_periods, monthly_payment, params, length_list
    if  length_list < 3:
        print('Incorrect parameters.')
        return
    elif args.type == None:
        print('Incorrect parameters')
        return
    elif args.type == 'diff' and monthly_payment in params:
        print('Incorrect parameters')
        return
    elif args.type == 'annuity' and (monthly_payment and loan_principle and num_of_periods in params):
        print('Incorrect parameters')
        return
    elif int(params[0]) < 0:
        print('Incorrect parameters')
        return
    elif int(params[1]) < 0:
        print('Incorrect parameters')
        return
    elif int(params[2]) < 0:
        print('Incorrect parameters')
        return

    if args.type == 'diff':
        i = loan_interest / 1200
        m = 1
        all_payment = 0
        for x in range(1, num_of_periods+1):
            monthly_payment = math.ceil((loan_principle / num_of_periods) + i * (loan_principle - (loan_principle * (m - 1))/num_of_periods))
            print(f'Month {x}: payment is {monthly_payment}')
            m += 1
            all_payment += monthly_payment
        overpayment = all_payment - loan_principle
        print(f'Overpayment = {overpayment}')
    if args.type == 'annuity' and (loan_principle and monthly_payment and loan_interest in params):
        i = loan_interest / 1200
        num_of_months = math.ceil(math.log((monthly_payment / (monthly_payment - i * loan_principle)), 1 + i))
        overpayment = math.ceil(monthly_payment * num_of_months - loan_principle)
        if num_of_months % 12 == 0:
            years = int(num_of_months / 12)
            print(f'It will take {years} years to repay this loan!\nOverpayment = {overpayment}')
        elif num_of_months < 12:
            print(f'It will take {num_of_months} months to repay this loan!\nOverpayment = {overpayment}')
        elif num_of_months > 11 and num_of_months % 12 != 0:
            years = math.floor(num_of_months / 12)
            months = int(num_of_months % 12)
            print(f'It will take {years} years and {months} months to repay this loan!\nOverpayment = {overpayment}')
    elif args.type == 'annuity' and (loan_principle and num_of_periods and loan_interest in params):
        i = loan_interest / 1200
        annuity = math.ceil(loan_principle * ((i * (math.pow(1+i, num_of_periods) / (math.pow(1+i, num_of_periods) - 1)))))
        overpayment = math.ceil(annuity * num_of_periods - loan_principle)
        print(f'Your monthly payment = {annuity}!\nOverpayment = {overpayment}')

    elif args.type == 'annuity' and (args.payment and args.periods and args.interest) in params:
        i = loan_interest / 1200
        loan_principle = math.ceil(monthly_payment / (i * (math.pow(1+i, num_of_periods) / (math.pow(1+i, num_of_periods) - 1))))
        overpayment = math.ceil(monthly_payment * num_of_periods - loan_principle)
        print(f'Your loan principal = {loan_principle}!\nOverpayment = {overpayment}')

calculate()
