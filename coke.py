total_price = 50
coins = [25,10,5]
while total_price > 0:
    print(f"total price: {total_price}")
    payment=int(input("insert coin: "))
    if payment in coins:
        total_price-=payment
    elif payment not in coins:
        print("invalid coin/ enter this coins(25,10,5)")
    else:
        continue
print(f"chnged ownd: {abs(total_price)}")