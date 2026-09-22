#Exercise 1
name = 'Rishi'
age = 20
capital = 5000

print(name, age, capital)

#Exercise 2
entry = 4400
exit = 4420

print(exit - entry)

#Exercise 3
lot_size = 0.05
contract_size = 100

print('ounces =',lot_size * contract_size)

#Exercise 4
capital = float(input("Enter your capital:"))

#Exercise 5
entry_price = float(input("Enter Entry price: "))
exit_price = float(input("Enter Exit price: "))
lot_size = float(input("Enter Lot size: "))

contract_size = 100

ounces = lot_size * contract_size

price_movement = exit_price - entry_price

pnl = ounces * price_movement

print("P&L:", pnl)


#Exercise 6
entry = 4426.63
exit = 4424.00
lot = 0.05
contract = 100
ounces = lot * contract
price_movement_l = exit - entry
price_movement_s = entry - exit
pnl_l= ounces * price_movement_l
pnl_s= ounces * price_movement_s

print("For long" ,pnl_l)
print("For short" ,pnl_s)