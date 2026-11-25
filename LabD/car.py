from gas_tank import GasTank
class Car:
    def __init__(self, capacity, consumption):
       self.tank = GasTank(capacity)
       self.consumption = consumption 
       
    def drive(self):
        if self.tank.current_fuel >= self.consumption:
            self.tank.consume_fuel(self.consumption)
            print("Vroom vroom")
        else:
            print("Out of fuel")

    def refuel(self):
        self.tank.refuel(100)
        print("Refueled. Good to go!")

