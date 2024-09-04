import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from project import df

# Define the tickers and shares held
tickers = [
    'ADYEY', 'AMZN', 'ASR', 'ATKR', 'AZO', 'BJ', 'BKNG', 'BRKB', 'CAAP', 'CFFN', 'CNM', 'CNSWF', 'CRL', 'CZMWY', 'DEO', 'DSGR',
    'ET', 'GFL', 'HSY', 'LVMUY', 'MGPI', 'OMAB', 'PWR', 'SLQT', 'SUBCY', 'TLT', 'TOITF', 'UBAB', 'V', 'VNT', 'XPO'
]
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]

# Assuming 'df' is a DataFrame containing all adjusted close prices for each stock
df = df.dropna()  # Drop rows with any NaN values to align data

# Calculate the value of each stock in the portfolio over time
stock_values = df.multiply(shares_held, axis=1)

# Calculate the total portfolio value for each day
total_portfolio_value = stock_values.sum(axis=1)

# Calculate the percentage contribution of each stock to the portfolio over time
percentage_contribution = stock_values.div(total_portfolio_value, axis=0) * 100

# Plot the percentage contribution of each stock over time
plt.figure(figsize=(14, 8))

for column in percentage_contribution.columns:
    plt.plot(percentage_contribution.index, percentage_contribution[column], label=column)

plt.title("Percentage Contribution of Each Stock to the Portfolio Over Time")
plt.xlabel("Date")
plt.ylabel("Percentage of Total Portfolio (%)")
plt.grid(True)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()
plt.show()