import inheritance


def main():
    marble = inheritance.Desk("Desk", 2, "Marble", 35, 100, 33, "Both Sides", 3, 1789.93)
    print ("Item: " + marble.get_product())
    print ("Quantity: " + str(marble.get_quantity()))
    print ("Material: " + marble.get_material())
    print ("Dimensions: " + str(marble.get_item_dimensions()))
    print ("Drawer(s) Location: " + marble.get_location())
    print ("Drawer(s): " + str(marble.get_drawers()))
    print ("Price: " + "${:0,.2f}".format(marble.get_price()))
    print("\n")

    print marble

main()
