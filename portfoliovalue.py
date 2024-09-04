from project import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = [
    'ADYEY', 'AMZN', 'ASR', 'ATKR', 'AZO', 'BJ', 'BKNG', 'BRKB', 'CAAP', 'CFFN', 'CNM', 'CNSWF', 'CRL', 'CZMWY', 'DEO', 'DSGR',
    'ET', 'GFL', 'HSY', 'LVMUY', 'MGPI', 'OMAB', 'PWR', 'SLQT', 'SUBCY', 'TLT', 'TOITF', 'UBAB', 'V', 'VNT', 'XPO'
]
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]

# Print the number of shares owned for each ticker
print("Number of Shares Owned for Each Ticker:")
for ticker, shares in zip(tickers, shares_held):
    print(f"{ticker}: {shares} shares")

df = df.dropna()

# Calculate the daily portfolio value
portfolio_values = df.multiply(shares_held, axis=1).sum(axis=1)

# Plot the portfolio value over time
x = print(df.tail())
plt.figure(figsize=(12, 6))
plt.plot(portfolio_values, label="Portfolio Value", color="blue")
plt.title("Portfolio Value Over Time")
plt.xlabel("Date")
plt.ylabel("Portfolio Value (in $)")
plt.grid(True)
plt.tight_layout()
plt.show()