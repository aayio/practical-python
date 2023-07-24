# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
base_payment = 2684.11
extra_payment = 1000.0
total_paid = 0.0
months = 0

while principal > 0:
    months += 1

    if months <= 12:
        total_payment = base_payment + extra_payment
    else:
        total_payment = base_payment
    
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment

print('total paid', round(total_paid, 2))
print('months', months)