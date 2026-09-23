symbol = "XAUUSD"

# Upgraded structure: List of dictionaries
# Each candle is a self-contained object holding its own keys and values
candles = [
    {
        "name": "Candle 1",
        "open": 4420.50,
        "high": 4435.20,
        "low": 4415.80,
        "close": 4430.10
    },
    {
        "name": "Candle 2",
        "open": 4430.10,
        "high": 4442.00,
        "low": 4425.50,
        "close": 4438.70
    },
    {
        "name": "Candle 3",
        "open": 4438.70,
        "high": 4450.00,
        "low": 4430.20,
        "close": 4445.80
    }
]

print(f"Symbol: {symbol}")

# Because we are using dictionaries, we don't need the 'ohlc' index mapper anymore.
# We can also use a 'for' loop instead of hardcoding [0], [1], [2].
for candle in candles:
    print(f"\n{candle['name']}")
    print(f"Open: {candle['open']:.2f}")
    print(f"High: {candle['high']:.2f}")
    print(f"Low:  {candle['low']:.2f}")
    print(f"Close: {candle['close']:.2f}")