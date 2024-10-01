import math
import argparse

parser = argparse.ArgumentParser(description="Compute all the parameters of the loan")

# Add arguments
parser.add_argument("--type", help="Set mode for annuity or differentiated payments")
parser.add_argument("--principal", type=float, help="The loan principal")
parser.add_argument(
    "--periods",
    type=int,
    help="Denotes the number of months needed to repay the loan",
)
parser.add_argument(
    "--interest", type=float, help="Interest is specified without a percent sign"
)
parser.add_argument("--payment", type=float, help="The annuity payment")

# Parse the arguments
args = parser.parse_args()

if args.type == None:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif args.interest == None:
    print("Incorrect parameters", len(vars(args)), vars(args))
elif (
    args_length_with_values := len(
        {k: v for k, v in vars(args).items() if v is not None}
    )
) < 4:
    print("Incorrect parameters")
elif any(v < 0 for v in vars(args).values() if isinstance(v, (int, float))):
    print("Incorrect parameters")
elif args.type == "diff" and args.payment == None:
    P = args.principal
    n = args.periods
    i = args.interest
    i /= 100  # convert the interest rate to decimals
    i /= 12  # convert the annual interest rate to monthly interest rate
    cumulative_paid = 0
    for m in range(1, args.periods + 1):
        D_m = P / n + i * (P - (P * (m - 1) / n))
        print(f"Month {m}: payment is {math.ceil(D_m)}")
        cumulative_paid += math.ceil(D_m)
    print()
    print(f"Overpayment = {round(cumulative_paid - P)}")
elif args.periods == None:
    A = args.payment
    i = args.interest
    i /= 100  # convert the interest rate to decimals
    i /= 12  # convert the annual interest rate to monthly interest rate
    P = args.principal
    log_argument = A / (A - i * P)
    n = math.log(log_argument, 1 + i)
    n = math.ceil(n)
    num_years = n // 12
    num_months = n % 12
    years_noun = "years" if num_years != 1 else "year"
    months_noun = "months" if num_months != 1 else "month"
    if num_years != 0 and num_months != 0:
        print(
            f"It will take {num_years} {years_noun} and {num_months} {months_noun} to repay this loan!"
        )
    elif num_years == 0:
        print(f"It will take {num_months} {months_noun} to repay this loan!")
    elif num_months == 0:
        print(f"It will take {num_years} {years_noun} to repay this loan!")

    print(f"Overpayment = {round(n * A - P)}")
elif args.payment == None:
    n = args.periods
    i = args.interest
    i /= 100  # convert the interest rate to decimals
    i /= 12  # convert the annual interest rate to monthly interest rate
    P = args.principal
    A = ((i * (1 + i) ** n) / ((1 + i) ** n - 1)) * P
    print(f"Your monthly payment = {math.ceil(A)}!")
    print(f"Overpayment = {round(math.ceil(A) * n - P)}")

elif args.principal == None:
    A = args.payment
    n = args.periods
    i = args.interest
    i /= 100  # convert the interest rate to decimals
    i /= 12  # convert the annual interest rate to monthly interest rate
    P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {round(P)}!")
    print(f"Overpayment = {math.ceil(A * n - P)}")
