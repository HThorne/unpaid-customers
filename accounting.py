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
