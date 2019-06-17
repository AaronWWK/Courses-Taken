
"""
Claculate the remaining balance at the end of the year

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal


"""
"""Problem 1"""
# for i in range(12):
#     balance = balance + annualInterestRate/12*balance
#     balance = balance*(1- monthlyPaymentRate)
#
# print('Remaining balance:',round(balance,2))
#
#
# for i in range(12):
#     balance = balance + balance*annualInterestRate/12
#     balance = balance * (1 - monthlyPaymentRate)
#
# print('Remaining Balance:',round(balance,2


"""Problem2"""
# Paste your code into this box
# lp =10  # The starting point of lowestpayment.
# a=0
# b0 = balance
# while b0 > 0:
#     a +=1
#     lp +=10
#     b0=balance
#     for i in range(12):
#         b0 = b0 - lp
#         b0 = b0 + annualInterestRate/12*b0
# print(lp)


#
# balance = 3329
# annualInterestRate = 0.2
# End_balance = balance
# for pay in range(10,balance,10):
#     End_balance = balance
#     for i in range(12):
#         End_balance = End_balance - pay
#         End_balance = End_balance*(annualInterestRate/12 + 1)
#
#     if End_balance <= 0:
#         print('Lowest Payment:',pay)
#         break


balance = 320000
annualInterestRate = 0.2


def lp(b,air):
    lb = b/12.0
    ub = b*(1+air)**12/12.0
    def lowest_pay(lb,ub):
        End_balance = b
        lp = (lb+ub)/2
        for i in range(12):
            End_balance = End_balance - lp
            End_balance = End_balance*(air/12 + 1)
        if End_balance > 0.01:
            lb2 = lp

            return lowest_pay(lb2,ub)
        elif End_balance < -0.01:
            ub2 = lp
            return lowest_pay(lb,ub2)
        else:
            return lp
    return round(lowest_pay(lb,ub),2)

print('Lowest Payment:',lp(balance,annualInterestRate))
