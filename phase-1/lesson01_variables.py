product_name = "Mahshahr Milk"
qty = 2
unit_price = 45000
packaging_fee = 5000
has_stock = True
total = unit_price * qty + packaging_fee
print(f"Product: {product_name} | Qty: {qty} | Total: {total} toman | In stock: {has_stock}")
print(10 / 2) # 5.0 because this is a float division
print(10 // 3) # 3 it is a int and it is rounded down 3.3333... to the nearest integer
print("10" + "5") # "105" it is a string concatenation
print(10 + 5) # 15
print(type(3.0)) # <class 'float'>


# "45000" * 2 is duplicating the string "45000" two times, resulting in "4500045000". which can be have wrong output if we want to calculate the total price. 