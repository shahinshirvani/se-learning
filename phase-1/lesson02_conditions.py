print(7 == 7.0) # Predict: True they have different class but the value is equal
print(7 == "7") # Perdict False  as they have different class
print(not (3 > 2 and 2 > 5)) # Predict: True
print(bool(0), bool(""), bool("False"), bool([])) # False, False, True, False
print(10 > 5 > 2) # Predict: True

def shipping_calculation(subtotal, is_vip):
    if subtotal >= 500000:
        shipping_fee = 0
    elif subtotal >= 150000:
        shipping_fee = 20000
    elif  150000 > subtotal > 0:
        shipping_fee = 35000
    else:
        shipping_fee = None
    if shipping_fee and is_vip:
        shipping_fee = shipping_fee // 2
    print(f"Subtotal: {subtotal} | VIP: {is_vip} | Shipping: {shipping_fee}")
    
shipping_calculation(500_000,True)
shipping_calculation(500_000,False)
shipping_calculation(150000,True)
shipping_calculation(150000,False)
shipping_calculation(0,True)
shipping_calculation(0,False)
shipping_calculation(-1,True)
shipping_calculation(-1,False)
shipping_calculation(149999,False)
shipping_calculation(149999,True)
shipping_calculation(499999,True)
shipping_calculation(499999,False)
# predict shipping with subtotal 150000 and is_vip true is 10000
# predict shipping with subtotal 149999 and is_vip true is 17500
# predict shipping with subtotal -1 and is_vip true is None
# predict shipping with subtotal 0 and is_vip true is None


subtotal = 600000
if subtotal >= 500000:
    shipping = 0
elif subtotal >= 150000:
    shipping = 20000
else:
    shipping = 35000
print(shipping)

# it is wrong because shipping should be shipping should 0 but because the first condition is True so the it did not reach the second condition
# I fixed and removed the buggy version

# for running subtotal = "150000" TypeError: '>=' not supported between instances of 'str' and 'int'
# for running subtotal = None TypeError: '>=' not supported between instances of 'NoneType' and 'int'

# Why doesn't if shipping_fee and is_vip: crash when shipping_fee is None: because shipping_fee is None mean it is false so never reach to if 

# In Trap 1, 45000 == "45000" silently returned False, but "150000" >= 500000 crashes. Which behavior is safer in a production shop, and why?: the second one. it is better to crashed that we do not understand the issue