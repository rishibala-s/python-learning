#Exercise 1
price= float(input("Enter XAUUSD price:"))

if price > 4500:
    print("Price is above 4500")

#Exercise 2
price= float(input("Enter XAUUSD price:"))

if price > 4400:
    print("BUY ZONE")
else :
    print("NO TRADE")

#Exercise 3
price= float(input("Enter XAUUSD price:"))
if price > 4500 :
    print("STRONG BUY")
elif price > 4400:
    print("BUY")
elif price > 4300 :
    print("NEUTRAL")
else :
    print("SELL")

#Exercise 4
trend = "bullish"
price = 4450

if trend == "bullish":
    if price > 4400:
        print("BUY")
    else:
        print("WAIT")
else:
    print("NO TRADE")

#Exercise 5
signal=input("Enter signal: ").lower()
match signal:
    case "buy":
        print("Execute BUY order")
    case "sell":
        print("Execute SELL order")
    case "hold":
        print("HOLD")
    case _:
        print("unknown signal")

#Exercise 6
prices = [4300, 4350, 4400, 4450, 4500]

for price in prices :
    if price > 4400:
        print("BUY")
    else:
        print("NO TRADE")

#Exercise 7
price = 4300

while price <=4500:
    print(price)
    price+=100

#Exercise 8
prices = [4300, 4350, 4400, 4450, 4500, 4550]

for price in prices:
    print("Checking:", price)

    if price >= 4450:
        print("Target reached")
        break

#Exercise 9
prices = [4300, 4350, 4400, 4450, 4500]

for price in prices:

    if price == 4400:
        print("Skipping:", price)
        continue

    if price > 4400:
        print(price, "BUY")
    else:
        print(price, "NO TRADE")

#Exercise 10
prices = [4280, 4320, 4380, 4420, 4480, 4550]

for price in prices:

    if price == 4400:
        print("SKIPPED")
        continue

    elif price > 4500:
        print("STRONG BUY")

    elif price == 4550:
        print("TARGET REACHED")
        break

    elif price > 4400 :
        print("BUY")

    elif price > 4300 :
        print("NEUTRAL")

    else:
        print("SELL")
