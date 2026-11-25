
from cashregister import CashRegister
cash = CashRegister()
def main():
    cash.addItem(6)
    cash.addItem(9.3)
    cash.addItem(99.99)
    cash.addItem(1)
    print(f"{cash.getTotal():.2f}")
    cash.undo()
    print(f"{cash.getTotal():.2f}")

if __name__ == "__main__":
    main()