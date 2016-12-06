import inheritance


def main():
    chair = inheritance.OfficeFurniture("Leather Chair", 3, "Leather", 35, 35, 45, 69.99)
    print ("Item: " + chair.get_product())
    print ("Quantity: " + str(chair.get_quantity()))
    print ("Material: " + chair.get_material())
    print ("Dimensions " + str(chair.get_item_dimensions()) + " sq.in.")
    print ("Price: " + "${:0,.2f}".format(chair.get_price()))
    print("\n")

    print chair

main()
