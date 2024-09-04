# Import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import norm

# Load Data into a Single DataFrame
ADYEY = pd.read_csv('CSVFiles/ADYEY.csv', parse_dates=['Date'], index_col='Date')
ADYEY = ADYEY.resample('D').last().dropna()
AMZN = pd.read_csv('CSVFiles/AMZN.csv', parse_dates=['Date'], index_col='Date')
AMZN = AMZN.resample('D').last().dropna()
ASR = pd.read_csv('CSVFiles/ASR.csv', parse_dates=['Date'], index_col='Date')
ASR = ASR.resample('D').last().dropna()
ATKR = pd.read_csv('CSVFiles/ATKR.csv', parse_dates=['Date'], index_col='Date')
ATKR = ATKR.resample('D').last().dropna()
AZO = pd.read_csv('CSVFiles/AZO.csv', parse_dates=['Date'], index_col='Date')
AZO = AZO.resample('D').last().dropna()
BJ = pd.read_csv('CSVFiles/BJ.csv', parse_dates=['Date'], index_col='Date')
BJ = BJ.resample('D').last().dropna()
BKNG = pd.read_csv('CSVFiles/BKNG.csv', parse_dates=['Date'], index_col='Date')
BKNG = BKNG.resample('D').last().dropna()
BRKB = pd.read_csv('CSVFiles/BRK-B.csv', parse_dates=['Date'], index_col='Date')
BRKB = BRKB.resample('D').last().dropna()
CAAP = pd.read_csv('CSVFiles/CAAP.csv', parse_dates=['Date'], index_col='Date')
CAAP = CAAP.resample('D').last().dropna()
CFFN = pd.read_csv('CSVFiles/CFFN.csv', parse_dates=['Date'], index_col='Date')
CFFN = CFFN.resample('D').last().dropna()
CNM = pd.read_csv('CSVFiles/CNM.csv', parse_dates=['Date'], index_col='Date')
CNM = CNM.resample('D').last().dropna()
CNSWF = pd.read_csv('CSVFiles/CNSWF.csv', parse_dates=['Date'], index_col='Date')
CNSWF = CNSWF.resample('D').last().dropna()
CRL = pd.read_csv('CSVFiles/CRL.csv', parse_dates=['Date'], index_col='Date')
CRL = CRL.resample('D').last().dropna()
CZMWY = pd.read_csv('CSVFiles/CZMWY.csv', parse_dates=['Date'], index_col='Date')
CZMWY = CZMWY.resample('D').last().dropna()
DEO = pd.read_csv('CSVFiles/DEO.csv', parse_dates=['Date'], index_col='Date')
DEO = DEO.resample('D').last().dropna()
DSGR = pd.read_csv('CSVFiles/DSGR.csv', parse_dates=['Date'], index_col='Date')
DSGR = DSGR.resample('D').last().dropna()
ET = pd.read_csv('CSVFiles/ET.csv', parse_dates=['Date'], index_col='Date')
ET = ET.resample('D').last().dropna()
GFL = pd.read_csv('CSVFiles/GFL.csv', parse_dates=['Date'], index_col='Date')
GFL = GFL.resample('D').last().dropna()
HSY = pd.read_csv('CSVFiles/HSY.csv', parse_dates=['Date'], index_col='Date')
HSY = HSY.resample('D').last().dropna()
LVMUY = pd.read_csv('CSVFiles/LVMUY.csv', parse_dates=['Date'], index_col='Date')
LVMUY = LVMUY.resample('D').last().dropna()
MGPI = pd.read_csv('CSVFiles/MGPI.csv', parse_dates=['Date'], index_col='Date')
MGPI = MGPI.resample('D').last().dropna()
OMAB = pd.read_csv('CSVFiles/OMAB.csv', parse_dates=['Date'], index_col='Date')
OMAB = OMAB.resample('D').last().dropna()
PWR = pd.read_csv('CSVFiles/PWR.csv', parse_dates=['Date'], index_col='Date')
PWR = PWR.resample('D').last().dropna()
SLQT = pd.read_csv('CSVFiles/SLQT.csv', parse_dates=['Date'], index_col='Date')
SLQT = SLQT.resample('D').last().dropna()
SUBCY = pd.read_csv('CSVFiles/SUBCY.csv', parse_dates=['Date'], index_col='Date')
SUBCY = SUBCY.resample('D').last().dropna()
TLT = pd.read_csv('CSVFiles/TLT.csv', parse_dates=['Date'], index_col='Date')
TLT = TLT.resample('D').last().dropna()
TOITF = pd.read_csv('CSVFiles/TOITF.csv', parse_dates=['Date'], index_col='Date')
TOITF = TOITF.resample('D').last().dropna()
UBAB = pd.read_csv('CSVFiles/UBAB.csv', parse_dates=['Date'], index_col='Date')
UBAB = UBAB.resample('D').last().dropna()
V = pd.read_csv('CSVFiles/V.csv', parse_dates=['Date'], index_col='Date')
V = V.resample('D').last().dropna()
VNT = pd.read_csv('CSVFiles/VNT.csv', parse_dates=['Date'], index_col='Date')
VNT = VNT.resample('D').last().dropna()
XPO = pd.read_csv('CSVFiles/XPO.csv', parse_dates=['Date'], index_col='Date')
XPO = XPO.resample('D').last().dropna()
AZO = pd.read_csv('CSVFiles/AZO.csv', parse_dates=['Date'], index_col='Date')
AZO = AZO.resample('D').last().dropna()



# Create a DataFrame for adjusted close prices
df = pd.DataFrame({
    'ADYEY_Price': ADYEY['Close'],
    'AMZN_Price': AMZN['Close'],
    'ASR_Price': ASR['Close'],
    'ATKR_Price': ATKR['Close'],
    'AZO_Price': AZO['Close'],
    'BJ_Price': BJ['Close'],
    'BKNG_Price': BKNG['Close'],
    'BRKB_Price': BRKB['Close'],
    'CAAP_Price': CAAP['Close'],
    'CFFN_Price': CFFN['Close'],
    'CNM_Price': CNM['Close'],
    'CNSWF_Price': CNSWF['Close'],
    'CRL_Price': CRL['Close'],
    'CZMWY_Price': CZMWY['Close'],
    'DEO_Price': DEO['Close'],
    'DSGR_Price': DSGR['Close'],
    'ET_Price': ET['Close'],
    'GFL_Price': GFL['Close'],
    'HSY_Price': HSY['Close'],
    'LVMUY_Price': LVMUY['Close'],
    'MGPI_Price': MGPI['Close'],
    'OMAB_Price': OMAB['Close'],
    'PWR_Price': PWR['Close'],
    'SLQT_Price': SLQT['Close'],
    'SUBCY_Price': SUBCY['Close'],
    'TLT_Price': TLT['Close'],
    'TOITF_Price': TOITF['Close'],
    'UBAB_Price': UBAB['Close'],
    'V_Price': V['Close'],
    'VNT_Price': VNT['Close'],
    'XPO_Price': XPO['Close'],
})


# Drop any rows with NaN values to ensure all data is valid
df = df.dropna()


tickers = [
    'ADYEY', 'AMZN', 'ASR', 'ATKR', 'AZO', 'BJ', 'BKNG', 'BRKB', 'CAAP', 'CFFN', 'CNM', 'CNSWF', 'CRL', 'CZMWY', 'DEO', 'DSGR',
    'ET', 'GFL', 'HSY', 'LVMUY', 'MGPI', 'OMAB', 'PWR', 'SLQT', 'SUBCY', 'TLT', 'TOITF', 'UBAB', 'V', 'VNT', 'XPO'
]
shares_held = [
    450, 45, 43, 100, 5, 250, 3, 78, 900, 2977, 450, 4, 50, 200, 100, 450, 1111, 300, 71, 60, 250, 400, 50, 4000, 1200, 300, 90, 600, 50, 450, 100
]

# Ensure data is aligned by dropping rows with NaN values
df = df.dropna()

# Calculate Daily Returns
daily_returns = df.pct_change(fill_method=None).dropna()

# Calculate the most recent 1-year rolling volatility for each ticker
rolling_volatilities = daily_returns.rolling(window=252).std() * np.sqrt(252)

# Extract the last value from the rolling volatility, which represents the annualized volatility over the past year
annualized_volatilities = rolling_volatilities.iloc[-1]

# Print out the calculated annualized volatilities for each ticker
print("Annualized Volatilities Based on the Most Recent 1-Year Distribution:")
for ticker, volatility in zip(tickers, annualized_volatilities):
    print(f"{ticker}: {volatility:.2f}%")

# Calculate Portfolio Weights Based on Shares Held
current_prices = df.iloc[-1].bfill()
portfolio_values = np.array(shares_held) * current_prices.values
portfolio_weights = portfolio_values / portfolio_values.sum()

# Calculate Portfolio Volatility Using Covariance Matrix and Weights
covariance_matrix = daily_returns.cov() * 252
portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(covariance_matrix, portfolio_weights)))

# Calculate the Weighted Average Volatility of Individual Assets
weighted_average_volatility = np.sum(portfolio_weights * annualized_volatilities)

# Calculate the Diversification Ratio
diversification_ratio = weighted_average_volatility / portfolio_volatility

# Output Results
print("Current Prices:\n", current_prices)
print("Daily Returns:\n", daily_returns.head())
print("Portfolio Weights:\n", portfolio_weights)
print(f"Diversification Ratio: {diversification_ratio:.2f}")
