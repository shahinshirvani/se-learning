print(7 == 7.0) # Predict: False
print(7 == "7") # Perdict False
print(not (3 > 2 and 2 > 5)) # Predict: True
print(bool(0), bool(""), bool("False"), bool([])) # False, False, True, False
print(10 > 5 > 2) # Predict: True


subtotal = 0
is_vip = True
shipping_fee = 0



if subtotal >= 500000:
    shipping_fee = 0
elif  500000 > subtotal >= 150000:
    shipping_fee = 20000
elif  150000 > subtotal > 0:
    shipping_fee = 35000
else:
    shipping_fee = None

if shipping_fee and is_vip:
    shipping_fee*=0.5

print(f"Subtotal: {subtotal} | VIP: {is_vip} | Shipping: {shipping_fee}")
# predict shipping with subtotal 150000 and is_vip true is 10000
# predict shipping with subtotal 149999 and is_vip true is 17500
# predict shipping with subtotal -1 and is_vip true is None
# predict shipping with subtotal 0 and is_vip true is None


subtotal = 600000
if subtotal >= 150000:
    shipping = 20000
elif subtotal >= 500000:
    shipping = 0
else:
    shipping = 35000
print(shipping)

# it is wrong because shipping should be shipping should 0 but because the first condition is True so the it did not reach the second condition


# QA Think: if subtotal be 150000.34, if it is 0.2, if it is 1000000000