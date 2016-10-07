"""This file should have our order classes in it."""

from random import randint

class AbstractMelonOrder(object):
    """Tracks melon orders and calculates totals."""

    def __init__(self, species, quantity, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.quantity = quantity
        self.shipped = False
        self.order_type = None
        self.tax = 0.00
        self.country_code = country_code

    def get_base_price(self):
        """Generating a random base price, between 5 - 9."""

        price = randint(5, 9)
        return price
        
    def get_total(self):
        """Calculate price."""

        price = self.get_base_price()

        if self.species.lower() == "christmas":
            price = price * 1.5

        total = (1 + self.tax) * self.quantity * price

        if self.order_type == "international" and self.quantity < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, quantity):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, quantity, 'USA')
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, quantity, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, 
                                                      quantity, 
                                                      country_code)
        self.order_type = "international"
        self.tax = 0.17

class GovernmentMelonOrder(AbstractMelonOrder):
    """Melons for The Government"""

    passed_inspection = None

    def mark_inspection(self, passed):
        """Changes inspection status to your inspection results (True or False).
        """        

        self.passed_inspection = passed
