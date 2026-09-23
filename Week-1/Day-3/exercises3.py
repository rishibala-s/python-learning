#Exercise 1
def check_market():
  pass
check_market()

#Exercise 2
prices = [4300, 4350, 4400, 4450]

for price in prices :
  print(price)

else:
  print("Price scan completed")

#Exercise 3
symbol = "XAUUSD"

print("First character:",symbol[0])
print("Last character:",symbol[-1])
print("Number of characters:", len(symbol))

#Exercise 4
side=input("Enter trading side:").lower()

print("Trading side:",side)

#Exercise 5
prices = [4400, 4420, 4450, 4480, 4500]

print("First price:",prices[0])
print("Third price:",prices[2])
print("Last price:",prices[-1])

#Exercise 6
prices = [4400, 4420, 4450]

prices[0] = 4395
prices.append(4480)

print(prices)

#Exercise 7
ohlc = (4420.50, 4435.20, 4415.80, 4430.10)

print("Open: ",ohlc[0])
print("High: ",ohlc[1])
print("Low: ",ohlc[2])
print("Close: ",ohlc[3])

#Exercise 8
symbols = {
    "XAUUSD",
    "EURUSD",
    "GBPUSD",
    "XAUUSD",
    "EURUSD"
}

print(symbols)
print(len(symbols))

#Exercise 9
candle = {
    "symbol": "XAUUSD",
    "open": 4420.50,
    "high": 4435.20,
    "low": 4415.80,
    "close": 4430.10
}

print("Symbol:",candle["symbol"])
print("Open:",candle["open"])
print("High:",candle["high"])
print("Low:",candle["low"])
print("Close:",candle["close"])

#Exercise 10
candle = {
    "symbol": "XAUUSD",
    "open": 4420.50,
    "high": 4435.20,
    "low": 4415.80,
    "close": 4430.10
}

candle["close"]= 4435.50
candle["volume" ]= 1250
print(candle)
