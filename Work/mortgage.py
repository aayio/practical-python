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
    
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment

print('total paid', round(total_paid, 2))
print('months', months)

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid?
# total paid 880074.1
# months 310