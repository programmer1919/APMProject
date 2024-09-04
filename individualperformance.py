import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from project import df

# Ensure that data is aligned by dropping rows with any NaN values
df = df.dropna()

# Normalize each stock's price to start at 100% for better comparison
normalized_df = (df / df.iloc[0]) * 100

# Plot the normalized performance of each stock
plt.figure(figsize=(14, 8))

for column in normalized_df.columns:
    plt.plot(normalized_df.index, normalized_df[column], label=column)

plt.title("Performance of Each Stock in the Portfolio")
plt.xlabel("Date")
plt.ylabel("Performance (%)")  # Y-axis label updated to indicate percentage
plt.grid(True)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)
plt.tight_layout()

# Set y-axis to show percentage
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

plt.show()

