# Import necessary libraries
from project import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



# Calculate Daily Returns
daily_returns = df.pct_change(fill_method=None).dropna()

# Standardize the returns
scaler = StandardScaler()
standardized_returns = scaler.fit_transform(daily_returns)

# Perform PCA
pca = PCA()
pca.fit(standardized_returns)

# Explained Variance Plot
plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o', linestyle='--')
plt.title('Cumulative Explained Variance by Principal Components')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.grid(True)
plt.show()

# Plot the Correlation Matrix using a heatmap with enhanced aesthetics
plt.figure(figsize=(16, 12))
sns.heatmap(daily_returns.corr(), annot=True, annot_kws={"size": 8}, cmap="coolwarm", vmin=-1, vmax=1, cbar_kws={"shrink": 0.75})
plt.title('Correlation Matrix of Basket Components', fontsize=16)
plt.xticks(fontsize=10, rotation=45, ha="right")
plt.yticks(fontsize=10, rotation=0)
plt.tight_layout()
plt.show()

# Visualizing the Principal Components
pca_components = pd.DataFrame(pca.components_, columns=daily_returns.columns)

plt.figure(figsize=(16, 8))
sns.heatmap(pca_components, cmap='coolwarm', annot=True, annot_kws={"size": 8}, vmin=-1, vmax=1)
plt.title('Principal Component Loadings')
plt.xlabel('Features')
plt.ylabel('Principal Components')
plt.xticks(fontsize=10, rotation=45, ha="right")
plt.tight_layout()
plt.show()
