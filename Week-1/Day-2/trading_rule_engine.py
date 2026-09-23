price = float(input("current enter XAUUSD price:"))
trend = input("market trend (bullish ,bearish ,sideways):").lower()

if trend == "bullish":
    if price >= 4550:
        print("TARGET REACHED")

    elif price > 4500:
        print("STRONG BUY")
    
    elif price > 4400:
        print("BUY")

    else:
        print("WAIT")

elif trend == "bearish":
    if price < 4300 :
        print("STRONG SELL")
    
    elif price < 4400 :
        print("SELL")

    else:
        print("WAIT")


elif trend == "sideways":
    print("NO TRADE")

else:
    print("INVALID TREND ")