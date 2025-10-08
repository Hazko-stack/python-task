
print("ES Companies ortal - Cashier App 3")
print("=================================================")
stock = 50
while True:
    name = input("Input item's name [5..30 characters] : ")
    if len(name) in range(5,30):
        break
while True:
    price = float(input("Input item's price [use decimal numbers | 10.0 - 2000.0]: $ "))
    if price > 10.0 and price <2000.0:
        break
while True:
    print("What will you do?")
    print("====================")
    print("1. Sell item") 
    print("2. Restock item") 
    print("3. Exit")
    opt = int(input("Choose : "))
    if opt == 1:
        if stock == 0:
            print("The item is out of stock, please restock!") 
            break
        else:
            while True: 
                try: 
                    qty = int(input(f"Input item's quantity [1..{stock}] : "))
                    if qty < stock and qty > 1:
                        stock = stock - qty
                        break
                    elif qty > stock:
                        print("Ouf of stock!")
                except ValueError:
                    print("Input must be number!")
            while True:
                disc = int(input("Input item's discount  [0..50] : "))
                if disc in range (0,50):
                    break
            total = price-qty*(100-disc)/100
        print("ES Companies Portal - Invoice") 
        print("===============================") 
        print(f"item's name \t\t: {name}") 
        print(f"item's price \t\t: {price}") 
        print(f"item's quantity \t: {qty}") 
        print(f"item's discount \t: {disc}%") 
        print(f"\nYou have to pay ${total}")
        while True:
            money = float(input(f"Input your money [use decimal numbers | min {total}] : $ "))
            if money >= total :
                change = money - total
                break
        print("\n\nThanks for purchasing!")
        if change > 0 :
            print(f"Your change : {change}$")
    elif opt == 2:
        if stock > 100:
            print("The item's stock is full, please sell it!")
        else:
            while True:
                add = int(input(f"Input stock to add [1..{100-stock}] : "))
                if add >= 1 and add <= (100-stock):
                    stock = stock + add
                    print("\nSuccess add stock!")
                    break
    else:
        print("Thanks for using this application :)")
        break            

