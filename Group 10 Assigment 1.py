print("Welcome to the Blue Station")
print("Menu:")
print("G: Gas")
print("O: Oil")

choice = input("Please enter your choice (G/g or O/o): ")

if choice != "G" and choice != "g" and choice != "O" and choice != "o":
    print("Invalid input, you should enter g/G or o/O")
else:
    province = input("Enter your province abbreviation (e.g., AB, ON): ")

    gst_rate = 0
    valid_province = False

    if province == "AB" or province == "ab":
        gst_rate = 0.05
        valid_province = True
    elif province == "BC" or province == "bc":
        gst_rate = 0.05
        valid_province = True
    elif province == "MB" or province == "mb":
        gst_rate = 0.05
        valid_province = True
    elif province == "NT" or province == "nt":
        gst_rate = 0.05
        valid_province = True
    elif province == "NU" or province == "nu":
        gst_rate = 0.05
        valid_province = True
    elif province == "QC" or province == "qc":
        gst_rate = 0.05
        valid_province = True
    elif province == "SK" or province == "sk":
        gst_rate = 0.05
        valid_province = True
    elif province == "YT" or province == "yt":
        gst_rate = 0.05
        valid_province = True
    elif province == "ON" or province == "on":
        gst_rate = 0.13
        valid_province = True
    elif province == "PE" or province == "pe":
        gst_rate = 0.15
        valid_province = True
    elif province == "NB" or province == "nb":
        gst_rate = 0.15
        valid_province = True
    elif province == "NS" or province == "ns":
        gst_rate = 0.15
        valid_province = True
    else:
        print("Wrong province entered. Program ends now.")

    if valid_province:
        if choice == "O" or choice == "o":
            cases_input = input("Enter number of oil cases: ")

            if cases_input.isdigit():
                cases = int(cases_input)
                litres = cases * 12
                price_per_litre = 1.27
                original_price = price_per_litre

                if cases > 8:
                    price_per_litre = price_per_litre * 0.90
                subtotal = litres * price_per_litre
                gst = subtotal * gst_rate
                total = subtotal + gst
                print("You selected: Oil")
                print("Total litres purchased: " + str(litres))

                if cases > 8:
                    print("Price before discount: $" + str(round(original_price, 2)) + " per litre")
                print("Price after discount: $" + str(round(price_per_litre, 2)) + " per litre")
                print("Oil Purchase Summary:")
                print("Subtotal: $" + str(round(subtotal, 2)))
                print("GST: $" + str(round(gst, 2)))
                print("Total Cost: $" + str(round(total, 2)))
            else:
                print("Invalid number of cases entered. Please enter a whole number.")

        if choice == "G" or choice == "g":
            litres_input = input("Enter number of gas litres: ")

            if litres_input.replace(".", "", 1).isdigit():
                litres = float(litres_input)
                price_per_litre = 1.07
                original_price = price_per_litre

                if litres > 4000:
                    price_per_litre = price_per_litre * 0.90
                subtotal = litres * price_per_litre
                gst = subtotal * gst_rate
                total = subtotal + gst
                print("You selected: Gas")
                print("Total litres purchased: " + str(round(litres, 2)))
                
                if litres > 4000:
                    print("Price before discount: $" + str(round(original_price, 2)) + " per litre")
                print("Price after discount: $" + str(round(price_per_litre, 2)) + " per litre")
                print("Gas Purchase Summary:")
                print("Subtotal: $" + str(round(subtotal, 2)))
                print("GST: $" + str(round(gst, 2)))
                print("Total Cost: $" + str(round(total, 2)))
            else:
                print("Invalid number of litres entered. Please enter a numeric value.")