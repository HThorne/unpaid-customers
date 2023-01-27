# constant variable
MELON_COST = 1.00

def create_payment_mistake_report(sales_report_file):
    """Opens and reads sales files, finds and prints over/under paid sales"""

    # open file and set to variable to access
    sales_list = open(sales_report_file)

    # iterate over each line from file
    for sale in sales_list:
        sale = sale.rstrip()
        sale_info = sale.split("|")

        # assign each item to variable
        customer_name = sale_info[1]
        melon_qty = float(sale_info[2])
        amount_paid = float(sale_info[3])

        # Calculate what they should have paid
        expected = melon_qty * MELON_COST

        # Decide if over/under paid, print info if True
        if expected > amount_paid:
            underpaid_amt = expected - amount_paid
            print(f"{customer_name} underpaid by ${round(underpaid_amt, 2)}.")

        elif amount_paid > expected:
            overpaid_amt = amount_paid - expected
            print(f"{customer_name} overpaid by ${round(overpaid_amt, 2)}.")


# Call function for available order report
create_payment_mistake_report("customer-orders.txt")



# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
