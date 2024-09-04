from project import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Calculate Daily Returns
daily_returns = df.pct_change(fill_method=None).dropna()

# Calculate the Rolling Monthly Standard Deviations (using 21 trading days as a month)
rolling_std = daily_returns.rolling(window=21).std() * np.sqrt(252)

# Plot the Rolling Monthly Standard Deviations for each stock
plt.figure(figsize=(14, 8))
for column in rolling_std.columns:
    plt.plot(rolling_std.index, rolling_std[column], label=column)

plt.title('Rolling Monthly Standard Deviations')
plt.xlabel('Date')
plt.ylabel('Standard Deviation')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)
plt.tight_layout()
plt.show()