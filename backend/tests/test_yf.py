import yfinance as yf
ticker = yf.Ticker("NVDA")
hist = ticker.history(period="max")
print(f"NVDA Rows: {len(hist)}")
if len(hist) > 0:
    print(f"Start: {hist.index[0]}")
    print(f"End: {hist.index[-1]}")

ticker = yf.Ticker("JPM")
hist = ticker.history(period="max")
print(f"JPM Rows: {len(hist)}")
if len(hist) > 0:
    print(f"Start: {hist.index[0]}")
    print(f"End: {hist.index[-1]}")
