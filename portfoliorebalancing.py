import pandas as pd
import numpy as np
import os
from project import df

# Set the correct path to the CSV files folder
csv_folder_path = '/Users/zakariyaahmed/Documents/personal_projects/Project/CSVFiles'  # Update this path

# Define function to calculate volatility of each stock
def calculate_volatility(stock_prices):
    daily_returns = stock_prices.pct_change().dropna()
    volatility = daily_returns.std() * np.sqrt(252)  # Annualized volatility
    return volatility

# Load all CSV files (excluding SPY.csv and CSU.TO.csv) and calculate volatilities
stock_volatilities = {}

for file_name in os.listdir(csv_folder_path):
    if file_name.endswith('.csv') and file_name not in ['SPY.csv', 'CSU.TO.csv']:  # Exclude SPY.csv and CSU.TO.csv
        # Read the CSV file
        ticker = file_name.split('.')[0]
        file_path = os.path.join(csv_folder_path, file_name)
        stock_data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
        # Resample daily data and drop NaNs
        stock_data = stock_data.resample('D').last().dropna()
        # Calculate volatility
        volatility = calculate_volatility(stock_data['Close'])
        stock_volatilities[ticker] = volatility

# Display calculated volatilities
stock_volatilities_df = pd.DataFrame(list(stock_volatilities.items()), columns=['Ticker', 'Volatility'])
stock_volatilities_df.sort_values(by='Volatility', ascending=False, inplace=True)
stock_volatilities_df.reset_index(drop=True, inplace=True)

# Define the current shares held in the portfolio (excluding CSU.TO)
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 
    71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]  # Exclude SPY and CSU.TO if it was initially included

# Calculate the target weights for equal volatility contribution
inverse_volatility = 1 / stock_volatilities_df['Volatility']
total_inverse_volatility = inverse_volatility.sum()
target_weights = inverse_volatility / total_inverse_volatility

# Load the last available prices for each stock (excluding SPY and CSU.TO)
latest_prices = {}

for file_name in os.listdir(csv_folder_path):
    if file_name.endswith('.csv') and file_name not in ['SPY.csv', 'CSU.TO.csv']:  # Exclude SPY.csv and CSU.TO.csv
        ticker = file_name.split('.')[0]
        file_path = os.path.join(csv_folder_path, file_name)
        stock_data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
        # Resample daily data and drop NaNs
        stock_data = stock_data.resample('D').last().dropna()
        # Get the last available price
        latest_prices[ticker] = stock_data['Close'].iloc[-1]

# Convert the latest prices to a DataFrame for easier manipulation
latest_prices_df = pd.DataFrame(list(latest_prices.items()), columns=['Ticker', 'Latest Price'])

# Merge the new shares allocation with the latest prices
stock_allocation = stock_volatilities_df.merge(latest_prices_df, on='Ticker')

# Calculate current portfolio values based on current shares held
current_shares_held = np.array(shares_held)  # Current shares held provided earlier (excluding SPY and CSU.TO)
current_values = current_shares_held * stock_allocation['Latest Price'].values
current_total_value = current_values.sum()

# Calculate current weights
current_weights = current_values / current_total_value

# Calculate the target value for each stock in the portfolio
target_values = target_weights * current_total_value

# Calculate the difference between target value and current value
stock_allocation['Current Value'] = current_values
stock_allocation['Current Shares Held'] = current_shares_held
stock_allocation['Target Value'] = target_values
stock_allocation['New Shares Held'] = stock_allocation['Target Value'] / stock_allocation['Latest Price']
stock_allocation['Rebalance Shares'] = stock_allocation['New Shares Held'] - stock_allocation['Current Shares Held']

# Ensure net $0 change by adjusting the number of shares to buy/sell
def adjust_rebalance(stock_allocation):
    # Calculate the net value change
    net_value_change = (stock_allocation['Rebalance Shares'] * stock_allocation['Latest Price']).sum()

    while abs(net_value_change) > 1e-5:  # Allow a small tolerance for floating-point precision
        # Find the stock with the largest rebalance dollar amount
        largest_rebalance = stock_allocation.loc[stock_allocation['Rebalance Shares'].abs().idxmax()]
        ticker_to_adjust = largest_rebalance['Ticker']
        
        # Adjust rebalance shares by offsetting the net change
        adjustment = -net_value_change / largest_rebalance['Latest Price']
        stock_allocation.loc[stock_allocation['Ticker'] == ticker_to_adjust, 'Rebalance Shares'] += adjustment
        
        # Recalculate net value change
        net_value_change = (stock_allocation['Rebalance Shares'] * stock_allocation['Latest Price']).sum()
    
    return stock_allocation

# Adjust rebalancing shares to ensure net value change is zero
stock_allocation = adjust_rebalance(stock_allocation)

# Display the adjusted portfolio composition with the rebalancing shares
print("\nRebalancing Portfolio (excluding SPY and CSU.TO) with Net $0 Change:")
print(stock_allocation[['Ticker', 'Latest Price', 'Current Shares Held', 'Target Value', 'New Shares Held', 'Rebalance Shares']].sort_values(by='Ticker').reset_index(drop=True))

# Function to rebalance portfolio
def rebalance_portfolio(stock_allocation):
    rebalance_actions = []
    for index, row in stock_allocation.iterrows():
        shares_to_buy_or_sell = row['Rebalance Shares']
        ticker = row['Ticker']
        action = "Buy" if shares_to_buy_or_sell > 0 else "Sell"
        rebalance_actions.append((ticker, action, abs(shares_to_buy_or_sell)))
    
    return rebalance_actions

# Get rebalancing actions
rebalance_actions = rebalance_portfolio(stock_allocation)
print("\nRebalancing Actions Needed (excluding SPY and CSU.TO) with Net $0 Change:")
for ticker, action, shares in rebalance_actions:
    print(f"{action} {shares:.2f} shares of {ticker}")
