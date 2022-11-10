"""
name: Derek D'Arcy
Description: This program takes user input for number of boxes purchased and calculates a discount.
"""

num_purchased = int(input('Enter the number of packages purchased: '))
price = 99
subtotal = num_purchased * price
discount = 1

# set discount based on number purchased
if 10 <= num_purchased <= 19:
    discount = 0.9
elif 20 <= num_purchased <= 49:
    discount = 0.8
elif 50 <= num_purchased <= 99:
    discount = 0.7
elif 100 <= num_purchased:
    discount = 0.6

# perform calculations for the total with discount, and the discounted value
total_amount = subtotal * discount
discount_amount = subtotal - total_amount

# display discount and total amount formated to 2 decimal places with commas
print(f'Discount amount: ${discount_amount:,.2f}')
print(f'Total Amount: ${total_amount:,.2f}')


def add(a: int, b: int):
    return a + b
