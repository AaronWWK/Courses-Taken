

# ####第一版
# def lp(b):
#
#     def lowest_payment(lp):
#         b0=b
#         for i in range(12):
#             b0 = b0 - lp
#             b0 = b0 + 0.2/12*b0
#         if b0 > 0:
#             lp = lp+10
#             return lowest_payment(lp)
#         else:
#             return lp
#     return lowest_payment(10)
# print('Lowest Payment:',lp(3926))
#




##改进版

balance = 325

annualInterestRate = 0.18

# lp =10
# a=0
# def lowest_payment(balance,annualInterestRate):
#
#     global a
#     a +=1
#     print(a)
#     global lp
#     lp +=10
#     b0=balance
#     for i in range(12):
#         b0 = b0 - lp
#         b0 = b0 + annualInterestRate/12*b0
#     if b0 > 0:
#         return lowest_payment(balance,annualInterestRate)
#     else:
#         return lp
# print(lowest_payment(3926,0.2))
#
#


lp =10  # The starting point of lowestpayment.
a=0
b0 = balance
while b0 > 0:
    a +=1
    lp +=10
    b0=balance
    for i in range(12):
        b0 = b0 - lp
        b0 = b0 + annualInterestRate/12*b0
print(lp)
