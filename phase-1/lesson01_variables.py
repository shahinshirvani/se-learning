product_name = "Mahshahr Milk"
qty = 2
unit_price = 45000
packaging_fee = 5000
has_stock = True
total = unit_price * qty + packaging_fee
print(f"Product: {product_name} | Qty: {qty} | Total: {total} toman | In Stock: {has_stock}")
print(10 / 2) # 5.0 because this is a float division
print(10 // 3) # 3 it is a float and it is rounded down to the nearest integer
print("10" + "5") # "105" it is a string concatenation
print(10 + 5) # 15
print(type(3.0)) # <class 'float'>

# "45000" * 2 is not valid because you cannot multiply a string by an integer in this context. You would need to convert the string to an integer first, like this: int("45000") * 2.