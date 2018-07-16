"""Classes for melon orders."""
class AbstractMelonOrder():
    def __init__(self,species,qty,country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_total(self):
        base_price = 5
        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"
    country_code = "USA"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"


class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed