weapon_list = []

# =========================
# READ FILE
# =========================
def read_file():
    weapon_list.clear()
    try:
        with open("warehouse.txt", "r") as file:
            for line in file:
                data = line.strip().split("#")
                weapon = {
                    "id": data[0],
                    "name": data[1],
                    "lore": data[2],
                    "class": data[3],
                    "category": data[4],
                    "damage": int(data[5]),
                    "power": int(data[6]),
                    "enchantment": data[7:]
                }
                weapon_list.append(weapon)
    except FileNotFoundError:
        print("File not found.")

# =========================
# WRITE FILE
# =========================
def write_file():
    try:
        with open("warehouse.txt", "w") as file:
            for weapon in weapon_list:
                w_enchantment = "#".join(weapon["enchantment"])
                file.write(
                    f"{weapon['id']}#{weapon['name']}#{weapon['lore']}#"
                    f"{weapon['class']}#{weapon['category']}#"
                    f"{weapon['damage']}#{weapon['power']}#"
                    f"{w_enchantment}\n"
                )
    except FileNotFoundError:
        print("File not found.")

# =========================
# DISPLAY
# =========================
def display():
    if not weapon_list:
        print("Arsenal is empty.")
        return

    for weapon in weapon_list:
        print(f"Weapon ID : {weapon['id']}")
        print(f"Name      : {weapon['name']}")
        print(f"Lore      : {weapon['lore']}")
        print(f"Class     : {weapon['class']}")
        print(f"Category  : {weapon['category']}")
        print(f"Damage    : {weapon['damage']}")
        print(f"Power     : {weapon['power']}")
        print("--- Enchantments ---")
        for enchantment in weapon["enchantment"]:
            print(f"- {enchantment}")
        print()

# =========================
# DISPLAY SORTED
# =========================
def display_sorted():
    sorted_weapon = sorted(
        weapon_list,
        key=lambda x: int(x["id"][2:]),
        reverse=True
    )

    for weapon in sorted_weapon:
        print(f"Weapon ID\t: {weapon['id']}")
        print(f"Name\t\t: {weapon['name']}")
        print(f"Category\t: {weapon['category']}")
        print("--- Enchantments ---")
        for enchantment in weapon["enchantment"]:
            print(f"- {enchantment}")
        print()

# =========================
# ADD WEAPON
# =========================
def add_weapon():
    print("=== Add New Weapon ===")

    wid = input("Weapon ID (WPxx): ")
    for weapon in weapon_list:
        if weapon["id"] == wid:
            print("ID already exists!")
            return

    name = input("Name: ")
    lore = input("Lore: ")
    wclass = input("Class: ")
    category = input("Category: ")
    damage = int(input("Damage: "))
    power = int(input("Power: "))

    enchantment = []
    while True:
        ench = input("Add Enchantment (type 'done' to finish): ")
        if ench.lower() == "done":
            break
        enchantment.append(ench)

    weapon = {
        "id": wid,
        "name": name,
        "lore": lore,
        "class": wclass,
        "category": category,
        "damage": damage,
        "power": power,
        "enchantment": enchantment
    }

    weapon_list.append(weapon)
    write_file()
    print("Weapon added successfully.")

# =========================
# DISMANTLE WEAPON
# =========================
def dismantle_weapon():
    while True:
        display_sorted()
        wid = input("Input Weapon ID to Dismantle: ")

        for weapon in weapon_list:
            if weapon["id"] == wid:
                weapon_list.remove(weapon)
                write_file()
                print("Weapon dismantled.")
                return

        print("ID not found!")

# =========================
# MAIN PROGRAM
# =========================
read_file()

while True:
    print("===== WEAPON WAREHOUSE =====")
    print("1. View Arsenal")
    print("2. View Sorted Arsenal")
    print("3. Add Weapon")
    print("4. Dismantle Weapon")
    print("5. Exit")

    choice = input("Choose menu: ")

    if choice == "1":
        display()
    elif choice == "2":
        display_sorted()
    elif choice == "3":
        add_weapon()
    elif choice == "4":
        dismantle_weapon()
    elif choice == "5":
        print("Exit program.")
        break
    else:
        print("Invalid choice.")
