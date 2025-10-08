import random

while True:
    print("\n=== KKingFish Log System ===")
    print("1. Log a new catch")
    print("2. Exit")

    choose = input("Choose menu (1-2): ").strip()

    if choose =="1":
        while True:
            angler =input("input angler name: ")
            if len(angler) >3 and all(ch.isalpha() or ch.isspace() for ch in angler) : 
                break
            else:
                "name must be mo=re than 3 character and only contain letter and space"

        species_name=["Tuna", "Salmon", "Bass", "or Marlin" ]
        while True:
            species =input("input fish species")
            if species in species_name:
                break
            else:
                "wrong species"

        while True:
            weight=input("input fish weight: ")
            if weight >0 :
                break
            else: "Must be positive number"

        catch_location=["River", "Lake", "Lake", "Sea", "Pond"]
        while True:
            location=input("input catch location: ")
            if location in catch_location:
                break
            else:
                "Location not valid"

        rod_type=["Spinning", "Casting"]
        while True:
            rod=input("Rod type: ")
            if rod in rod_type:
                break
            else:
                "rod not valid"
        log_id= "KK" + str(random.randint(1000, 9999))

        if weight <5:
            category = "small fry"
        elif weight >=5 and weight<= 15:
            category = "Trophy fish"
        else: 
            category = "small fish"

        pounds = weight*2.20462

        # result
        print("log id:", log_id)
        print("Angler name:", angler)
        print("Fish species:", species)
        print("Catch location:", location)
        print("Rod type:", rod)
        print("========================")
        print("Weight(kg):", weight)
        print("Weight(lbs):", pounds)
        print("Size category:", category)

    elif choose == "2":
        print("Thank you for using KKIngfish Log System")
        break
    else:
        print("invalid menu, pliss choose 1 or 2")


        



                


   