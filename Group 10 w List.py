print("*** Welcome to Gas Station Program! ***")
print("G: Gas")
print("O: Oil")

choice = input("Enter your choice: ")

if choice != "G" and choice != "g" and choice != "O" and choice != "o":
    print("Invalid input, you should enter g/G or o/O")
else:
    province = input("Enter province abbreviation: ")

    gst_rate = 0
    valid_province = False

    five_percent = list(["AB", "ab", "BC", "bc", "MB", "mb", "NT", "nt", "NU", "nu", "QC", "qc", "SK", "sk", "YT", "yt"])
    thirteen_percent = list(["ON", "on"])
    fifteen_percent = list(["PE", "pe", "NB", "nb", "NS", "ns"])

    if province in five_percent:
        gst_rate = 0.05
        valid_province = True
    elif province in thirteen_percent:
        gst_rate = 0.13
        valid_province = True
    elif province in fifteen_percent:
        gst_rate = 0.15
        valid_province = True
    else:
        print("Invalid province entered. Program will now exit.")

    if valid_province:
        if choice == "G" or choice == "g":
            litres_input = input("Enter number of litres: ")
            litres = float(litres_input)
            price_per_litre = 1.07
            original_price = price_per_litre
            price_before_discount = litres * original_price
            if litres > 4000:
                price_per_litre = price_per_litre * 0.90
            price_after_discount = litres * price_per_litre
            gst = price_after_discount * gst_rate
            total = price_after_discount + gst
            print()
            print("Product: Gas")
            print("# Of Litres: " + str(litres))
            if litres > 4000:
                print("Price Before Discount: " + str(price_before_discount))
            print("Price After Discount: " + str(price_after_discount))
            print("GST: " + str(gst))
            print("Total Price: " + str(total))

        if choice == "O" or choice == "o":
            cases_input = input("Enter number of cases: ")
            cases = int(cases_input)
            litres = cases * 12
            price_per_litre = 1.27
            original_price = price_per_litre
            price_before_discount = litres * original_price
            if cases > 8:
                price_per_litre = price_per_litre * 0.90
            price_after_discount = litres * price_per_litre
            gst = price_after_discount * gst_rate
            total = price_after_discount + gst
            print()
            print("Product: Oil")
            print("# Of Litres: " + str(litres))
            if cases > 8:
                print("Price Before Discount: " + str(price_before_discount))
            print("Price After Discount: " + str(price_after_discount))
            print("GST: " + str(gst))
            print("Total Price: " + str(total))