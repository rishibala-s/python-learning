print('=' * 40)
print("      XAUUSD P&L CALCULATOR")
print('=' * 40)

entry_price = float(input("Entry price : "))
exit_price = float(input("Exit price : "))
lot_size = float(input("Lot size : "))

side = input("Side (enter 'buy' or 'sell'): ").lower()

contract_size = 100

position_size = lot_size * contract_size

print("Position size :", position_size)

if side == "buy":

    price_movement = exit_price - entry_price

elif side == "sell":

    price_movement = entry_price - exit_price

else:

    print("Invalid side! Please enter buy or sell.")
    exit()

print("Price Movement :", price_movement)

pnl = price_movement * position_size

if pnl > 0:

    print(f"P&L : ${pnl:.2f}")
    print("Result : PROFIT")

elif pnl < 0:

    print(f"P&L : ${pnl:.2f}")
    print("Result : LOSS")

else:

    print("P&L : $0.00")
    print("Result : BREAK-EVEN")