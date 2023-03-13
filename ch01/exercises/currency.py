rate = float(input("enter the exchange rate from Euro to US dollar: "))

amount = float(input("enter amount: "))
print(amount, type(amount))

new_amount = amount * rate
total= new_amount
print(total)

minus_fee = new_amount - 3.00
result = minus_fee
print(result)