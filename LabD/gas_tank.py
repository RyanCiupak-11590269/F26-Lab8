
class GasTank:

    def __init__(self, max_fuel):
        self.max_fuel = max_fuel
        self.current_fuel = max_fuel

    def consume_fuel(self, amount):
        self.current_fuel -= amount
        self.current_fuel = max(0, self.current_fuel);

    def refuel(self, amount):
        self.current_fueld += amount
        self.current_fueld = min(self.current_fuel, self.max_fuel)