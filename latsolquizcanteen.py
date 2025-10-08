

# Input nama item
while True:
    item_name = input("Masukkan nama barang (5-30 huruf): ")
    if item_name.isalpha() and 5 >= len(item_name) <= 30:
        break
    else:
        print("Nama tidak valid! Hanya huruf, 5-30 karakter.")

# Input harga item
while True:
    item_price = input("Masukkan harga barang (10-2000): ")
    if item_price.isdigit():
        item_price = int(item_price)
        if 10 <= item_price <= 2000:
            break
    print("Harga tidak valid! Masukkan angka 10-2000.")

# Stok awal
item_stock = 50

# Menu utama
while True:
    print("\n=== CanteenSunib Menu ===")
    print("1. Beli barang")
    print("2. Tambah stock")
    print("3. Keluar")

    choice = input("Pilih menu (1-3): ")

    if choice == "1":
        # Beli barang
        while True:
            qty = input(f"Masukkan jumlah barang (1-{item_stock}): ")
            if qty.isdigit():
                quantity = int(qty)
                if 1 <= quantity <= item_stock:
                    break
            print("Jumlah tidak valid!")

        while True:
            disc = input("Masukkan diskon (0-50): ")
            if disc.isdigit():
                discount = int(disc)
                if 0 <= discount <= 50:
                    break
            print("Diskon tidak valid!")

        total_price = item_price * quantity * (100 - discount) / 100

        print("\n=== INVOICE ===")
        print("Nama barang :", item_name)
        print("Harga satuan:", item_price)
        print("Jumlah      :", quantity)
        print("Diskon      :", discount, "%")
        print("Total bayar :", total_price)

        while True:
            pay = input("Masukkan jumlah uang: ")
            if pay.isdigit():
                money = int(pay)
                if money >= total_price:
                    break
            print("Uang kurang atau tidak valid!")

        item_stock -= quantity
        change = money - total_price
        print("Kembalian   :", change)

    elif choice == "2":
        # Tambah stock
        while True:
            add = input("Masukkan tambahan stock (1-50): ")
            if add.isdigit():
                add_stock = int(add)
                if 1 <= add_stock <= 50:
                    break
            print("Tambahan tidak valid!")

        item_stock += add_stock
        print("Success add to stock. Stock sekarang:", item_stock)

    elif choice == "3":
        print("Thanks for using the application")
        break

    else:
        print("Pilihan tidak valid! Coba lagi.")
