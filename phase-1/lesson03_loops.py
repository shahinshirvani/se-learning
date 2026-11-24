# a predict: 2,5,8
for i in range(2, 10, 3):
    print(i)

# b predict: 1+2+3+4=10
total = 0
for n in range(1, 5):
    total += n
print(total)

# c predict: 12
count = 0
while count < 10:
    count += 3
print(count)

# d predict 0,1,3
for i in range(6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

# e predict: cc, aa, tt
for ch in "cat":
    print(ch * 2)
    
    
    
def fake_api_call(attempt):
    return attempt >= 4     # succeeds on the 4th try    
    
attempt = 1
while attempt <= 5:
    print(f"waiting {attempt*2} s")
    if fake_api_call(attempt):
        print(f"succeeded after {attempt} attempts")
        break
    attempt += 1
    print("gave up after 5 attempts")    
    
    

def paginations(total_items):
    if total_items == 0: print('There is nothing to show')
    i=1
    page_size = 20
    page = 0
    while i <= total_items:
        if i % page_size == 0:
            page += 1
            i+= 1
            print(f"Page {page}: items: {((page-1)*page_size)+1}-{page*page_size}")
        elif i == total_items:
            print(f"Page {page}: items: {((page-1)*page_size)+1}-{i}")
            break
        else:
            i+= 1
            continue
                 
paginations(237)
paginations(240)
paginations(0)
    
    
attempt = 1
while attempt <= 3:
    print("trying", attempt)
    if attempt == 2:
        attempt += 1
        continue
    else:
        attempt += 1

# it stock in a loop as attempt never reach to the next value



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
    
    
subtotal = [500_000,500_000,150000,150000,0,0,-1,-1,149999,149999,499999,499999]
is_vip = [True,False,True,False ,True,False,True,False,False,True,True,False]
for i in range(len(subtotal)):
    shipping_calculation(subtotal[i],is_vip[i])
