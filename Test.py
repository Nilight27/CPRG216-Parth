#displaying + choosing menu
print("---------------------------------------------")
print(f"{'*** Welcome to Gas Station Program! ***' : ^45}")
print("---------------------------------------------")
print("Please select the type of purchase:")
print("G: Gas \nO: Oil")
option_selected = input(">>> ")

gas_selected = False
oil_selected = False
amount_check = False

list_1 = ["AB", "ab", "BC", "bc", "MB", "mb", "NT", "nt", "NU", "nu", "QC", "qc", "SK", "sk", "YT", "yt"]
ontario_checker = ["ON", "on"]

#checking which option was selected
if option_selected == "G" or option_selected == "g":
    print("You have chosen Gas")
    gas_selected = True
elif option_selected == "O" or option_selected == "o":
    print("You have chosen Oil")
    oil_selected = True
else:
    print("Invalid input, you should enter g/G or o/O")

#after selection branching
while (gas_selected == True or oil_selected == True) and amount_check == False:
    if gas_selected == True:
        amount_litres = int(input("Enter the number of litres of gas: "))
        if amount_litres > 0:
            province = input("Please enter a 2 letter province abbreviation: ")
            amount_check = True
        else:
            print("Number of gas litres should be > 0")
            exit()

    elif oil_selected == True:
        amount_cases = int(input("Enter # of cases of Oil: "))
        if amount_cases > 0:
            province = input("Please enter a 2 letter province abbreviation: ")
            amount_check = True
        else:
            print("Number of oil cases should be > 0")
            exit()
    else:
        print("Please enter a valid option")

#after amount + price calculator w/ discount
while amount_check == True:
    if gas_selected == True:
        price_litres = amount_litres * 1.07
        type_selected = "Gas"

        #province gst adder
        if province in list_1:
            gst = price_litres * 0.05
        elif province in ontario_checker:
            gst = price_litres * 0.13
        else:
            gst = price_litres * 0.15

        if amount_litres >= 4000:
            discount_price_litres = price_litres * 0.9
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Product    # of Litres    Price Before Discount    Price After Discount    GST   Total Price': ^100}")
            format_print = (
                type_selected,
                f"{amount_litres:.2f}",
                f"{price_litres:.2f}",
                f"{discount_price_litres:.2f}",
                f"{gst:.2f}",
                f"{(discount_price_litres + gst):.2f}"
            )
            format_string = ""
            for item in format_print:
                format_string += str(item) + "             "
            print(f"     {format_string : ^100}")
            print("----------------------------------------------------------------------------------------------------")
            print("Thank you for your business, Goodbye!")
            exit()
        else:
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Product    # of Litres    Price Before Discount    Price After Discount    GST   Total Price': ^100}")
            format_print = (
                type_selected,
                f"{amount_litres:.2f}",
                f"{price_litres:.2f}",
                f"{price_litres:.2f}",
                f"{gst:.2f}",
                f"{(price_litres + gst):.2f}"
            )
            format_string = ""
            for item in format_print:
                format_string += str(item) + "             "
            print(f"     {format_string : ^100}")
            print("----------------------------------------------------------------------------------------------------")
            print("Thank you for your business, Goodbye!")
            exit()

    else:
        amount_litres_oil = amount_cases * 12
        price_cases = amount_litres_oil * 1.27
        type_selected = "Oil"

        #province gst adder
        if province in list_1:
            gst = price_cases * 0.05
        elif province in ontario_checker:
            gst = price_cases * 0.13
        else:
            gst = price_cases * 0.15

        if amount_cases >= 8:
            discounted_price_cases = price_cases * 0.9
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Product    # of Litres    Price Before Discount    Price After Discount    GST   Total Price': ^100}")
            format_print = (
                type_selected,
                f"{amount_litres_oil:.2f}",
                f"{price_cases:.2f}",
                f"{discounted_price_cases:.2f}",
                f"{gst:.2f}",
                f"{(discounted_price_cases + gst):.2f}"
            )
            format_string = ""
            for item in format_print:
                format_string += str(item) + "             "
            print(f"     {format_string : ^100}")
            print("----------------------------------------------------------------------------------------------------")
            print("Thank you for your business, Goodbye!")
            exit()
        else:
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Product    # of Litres    Price Before Discount    Price After Discount    GST   Total Price': ^100}")
            format_print = (
                type_selected,
                f"{amount_litres_oil:.2f}",
                f"{price_cases:.2f}",
                f"{price_cases:.2f}",
                f"{gst:.2f}",
                f"{(price_cases + gst):.2f}"
            )
            format_string = ""
            for item in format_print:
                format_string += str(item) + "             "
            print(f"     {format_string : ^100}")
            print("----------------------------------------------------------------------------------------------------")
            print("Thank you for your business, Goodbye!")
            exit()