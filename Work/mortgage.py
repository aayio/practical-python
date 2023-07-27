# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0
total_paid = 0.0
months = 0

while principal > 0:
    months += 1

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        total_payment = base_payment + extra_payment
    else:
        total_payment = base_payment
    
    if total_payment >= principal:
        total_payment = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - total_payment
    
    total_paid = total_paid + total_payment
    # print(months, round(total_paid, 2), round(principal, 2))
    print(f'{months:>4} {total_paid:>11.2f} {principal:>11.2f}')

print('')
# print('total paid', round(total_paid, 2))
# print('months', months)
print(f'total paid: {total_paid:.2f} in {months} months')

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid?
# total paid 880074.1
# months 310

# While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
# 310 878199.2 0
# total paid 878199.2
# months 310