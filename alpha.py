import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.optimize import curve_fit
from project import df

# Load SPY data
spy = pd.read_csv('CSVFiles/SPY.csv', parse_dates=['Date'], index_col='Date')
spy = spy['Close'].resample('D').last().dropna()  # Resample and align with portfolio data

# Assuming 'df' is a DataFrame containing all adjusted close prices for each stock
df = df.dropna()  # Drop rows with any NaN values to align data

# Define the tickers and shares held
tickers = [
    'ADYEY', 'AMZN', 'ASR', 'ATKR', 'AZO', 'BJ', 'BKNG', 'BRKB', 'CAAP', 'CFFN', 'CNM', 'CNSWF', 'CRL', 'CZMWY', 'DEO', 'DSGR',
    'ET', 'GFL', 'HSY', 'LVMUY', 'MGPI', 'OMAB', 'PWR', 'SLQT', 'SUBCY', 'TLT', 'TOITF', 'UBAB', 'V', 'VNT', 'XPO'
]
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]

# Calculate the value of each stock in the portfolio over time
stock_values = df.multiply(shares_held, axis=1)

# Calculate the total portfolio value for each day
portfolio_values = stock_values.sum(axis=1)

# Ensure the data aligns by finding the intersection of dates
aligned_data = pd.concat([portfolio_values, spy], axis=1).dropna()
aligned_data.columns = ['Portfolio', 'SPY']

# Calculate daily returns for both portfolio and SPY
aligned_data['Portfolio_Return'] = aligned_data['Portfolio'].pct_change().dropna()
aligned_data['SPY_Return'] = aligned_data['SPY'].pct_change().dropna()

# Drop the NaN values created by percentage change calculation
aligned_data = aligned_data.dropna()

# Calculate the rolling 30-day variance (volatility) of portfolio and SPY returns
rolling_window = 30
aligned_data['Portfolio_Variance'] = aligned_data['Portfolio_Return'].rolling(window=rolling_window).var()
aligned_data['SPY_Variance'] = aligned_data['SPY_Return'].rolling(window=rolling_window).var()

# Define a function to model the variance relationship
def variance_model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the curve to the variance data
xdata = aligned_data['SPY_Variance'].dropna()
ydata = aligned_data['Portfolio_Variance'].dropna()

popt, _ = curve_fit(variance_model, xdata, ydata)

# Plot the variances and the fitted curve
#plt.figure(figsize=(10, 6))
#plt.scatter(xdata, ydata, alpha=0.5, label='Daily Variance Data')
#plt.plot(xdata, variance_model(xdata, *popt), color='red', label=f'Fitted Curve: {popt[0]:.4f}*x^2 + {popt[1]:.4f}*x + {popt[2]:.4f}')
#plt.title('Portfolio Variance vs. SPY Variance')
#plt.xlabel('SPY Variance')
#plt.ylabel('Portfolio Variance')
#plt.grid(True)
#plt.legend()
#plt.show()

# Output the fitted curve parameters
#print(f"Fitted Curve Parameters: a={popt[0]:.4f}, b={popt[1]:.4f}, c={popt[2]:.4f}")

# Regression analysis for alpha and beta
# Add a constant to the independent variable (SPY returns) for the regression intercept (alpha)
X = sm.add_constant(aligned_data['SPY_Return'])
y = aligned_data['Portfolio_Return']

# Perform linear regression
model = sm.OLS(y, X).fit()
alpha = model.params['const']
beta = model.params['SPY_Return']

# Output Results
print(f"Alpha of the Portfolio: {alpha:.4f}")
print(f"Beta of the Portfolio: {beta:.4f}")

# Plot the Portfolio vs SPY returns for visual verification
plt.figure(figsize=(10, 6))
plt.scatter(aligned_data['SPY_Return'], aligned_data['Portfolio_Return'], alpha=0.5)
plt.plot(aligned_data['SPY_Return'], model.predict(X), color='red', label=f'Regression Line (Alpha={alpha:.4f}, Beta={beta:.4f})')
plt.title('Portfolio Returns vs. SPY Returns')
plt.xlabel('SPY Returns')
plt.ylabel('Portfolio Returns')
plt.legend()
plt.grid(True)
plt.show()

# Define the risk-free rate directly in the code
risk_free_rate = 0.05  # Example: 1% risk-free rate

# Calculate the Sharpe ratio
portfolio_return = aligned_data['Portfolio_Return'].mean()
portfolio_std_dev = aligned_data['Portfolio_Return'].std()
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev

# Output the Sharpe ratio
print(f"Sharpe Ratio of the Portfolio: {sharpe_ratio:.4f}")
