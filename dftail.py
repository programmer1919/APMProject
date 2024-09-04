import pandas as pd
from project import df
# Assuming you have already loaded your data into the df DataFrame

# Define the tickers and number of shares held
tickers = [
    'ADYEY', 'AMZN', 'ASR', 'ATKR', 'AZO', 'BJ', 'BKNG', 'BRKB', 'CAAP', 'CFFN', 'CNM', 'CNSWF', 'CRL', 'CZMWY', 'DEO', 'DSGR',
    'ET', 'GFL', 'HSY', 'LVMUY', 'MGPI', 'OMAB', 'PWR', 'SLQT', 'SUBCY', 'TLT', 'TOITF', 'UBAB', 'V', 'VNT', 'XPO'
]
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]

# Get the most recent prices for each stock
current_prices = df.iloc[-1]  # Last row contains the most recent prices

# Calculate the current values held in each stock
current_values = current_prices * shares_held

# Convert the result to a DataFrame for easier readability
current_values_df = pd.DataFrame({
    'Ticker': tickers,
    'Shares Held': shares_held,
    'Current Price': current_prices.values,
    'Current Value': current_values.values
})

# Print the current values for each stock
print(current_values_df[['Ticker', 'Current Value']])
