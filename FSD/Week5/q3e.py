from q3 import CashRegister

register = CashRegister()

register.addItem(1)
register.addItem(2.90)
register.addItem(5.30)
print(register.getCount())
print(register.getTotal())
print(register.getPounds())
print("{0:.2f}" .format(register.giveChange(11)))