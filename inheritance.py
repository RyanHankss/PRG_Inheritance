class OfficeFurniture(object):
    """
        accepts product, material, width, length, height, price
    """
    def __init__(self, product, quantity, material, width, length, height, price):

        self.__product = product
        self.__quantity = quantity
        self.__material = material
        self.__width = width
        self.__length = length
        self.__height = height
        self.__price = price

# First Set

    def set_product(self, product):
        self.__product = product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_material(self, material):
        self.__material = material

    def set_width(self, width):
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def set_height(self, height):
        self.__height = height

    def set__price(self, price):
        self.__price = price

# Now get

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_material(self):
        return self.__material

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_item_price(self):
        return self.__price * self.__quantity

    def get_item_dimensions(self):
        return int((self.__length * self.__width * self.__height) ** .5)

    def __str__(self):
        chair_info = self.__product + " Quantity: " + str(self.__quantity) + " Dimensions: " + str(self.get_item_dimensions()) + " sq.in." + " Each: ${:0,.2f}".format(self.__price) + " Total: ${:0,.2f}".format(self.get_item_price())
        return chair_info

# desk Class


class Desk(OfficeFurniture):

    """
    Desk class extends the OfficeFurniture class and adds additional methods to include a desk with drawers

    """

    def __init__(self, product, quantity, material, width, length, height, location, drawers, price):
        OfficeFurniture.__init__(self, product, quantity, material, width, length, height, price)

        self.__location = location

        self.__drawers = drawers

    def set_location(self, location):
        self. __location = location

    def set_drawers(self, drawers):
        self.__drawers = drawers

    # Now get

    def get_location(self):
        return self.__location

    def get_drawers(self):
        return self.__drawers

    def __str__(self):
        desk_info = "Product: " + self.get_product() + " Quantity: " + str(self.get_quantity()) + " Material: " + self.get_material() + " Dimensions: " + str(self.get_item_dimensions()) + " sq.in. " + "Drawer(s) Location: " + self.__location + " Drawer(s): " + str(self.__drawers) + " Price Per Unit: " + "${:0,.2f}".format(self.get_price()) + " Total: " + "${:0,.2f}".format(self.get_item_price())
        return desk_info
