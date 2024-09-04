import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
from alpha import aligned_data

# Assuming aligned_data is already prepared as in the previous steps
X = aligned_data['SPY_Return'].values
y = aligned_data['Portfolio_Return'].values

# Standardize the X values (SPY returns) for better numerical stability in Bayesian modeling
X_standardized = (X - X.mean()) / X.std()

# Build the Bayesian regression model using Aesara
with pm.Model() as model:
    # Priors for the intercept (alpha) and slope (beta)
    alpha = pm.Normal('alpha', mu=0, sigma=1)
    beta = pm.Normal('beta', mu=0, sigma=1)
    
    # Likelihood (model) assuming a normal distribution of errors
    sigma = pm.HalfCauchy('sigma', beta=10)
    mu = alpha + beta * X_standardized
    likelihood = pm.Normal('y', mu=mu, sigma=sigma, observed=y)
    
    # Prior predictive checks
    prior_checks = pm.sample_prior_predictive()
    
    # Perform the sampling
    trace = pm.sample(2000, return_inferencedata=False, tune=1000)
    
    # Posterior predictive checks
    posterior_predictive = pm.sample_posterior_predictive(trace)
    
    # Convert the MultiTrace object to InferenceData within the model context
    idata = az.from_pymc3(trace=trace, prior=prior_checks, posterior_predictive=posterior_predictive)

# Summarize the posterior distributions
summary = az.summary(idata)
print(summary)

# Plot the posterior distributions
az.plot_trace(idata)
plt.show()

# Additional diagnostic plots
az.plot_posterior(idata)
plt.show()

# Prior predictive checks plot
az.plot_ppc(idata, group='prior')
plt.show()

# Posterior predictive checks plot
az.plot_ppc(idata, group='posterior')
plt.show()

# Detailed diagnostics
az.plot_rhat(idata)
plt.show()

az.plot_ess(idata)
plt.show()

az.plot_autocorr(idata)
plt.show()

# Pair plot of the posterior distributions
az.plot_pair(idata, kind='kde', marginals=True)
plt.show()

# Predictions and Uncertainty Intervals
alpha_samples = trace['alpha']
beta_samples = trace['beta']
predicted_y = alpha_samples.mean() + beta_samples.mean() * X_standardized

# 95% Highest Posterior Density (HPD) interval
hpd_interval = az.hdi(posterior_predictive, hdi_prob=0.95)

# Plot the predictions with uncertainty intervals
plt.figure(figsize=(10, 6))
plt.plot(X, y, 'o', label="Observed data")
plt.plot(X, predicted_y, label="Mean Prediction", color='red')
plt.fill_between(X, hpd_interval['y'].sel(hdi='lower'), hpd_interval['y'].sel(hdi='upper'), color='gray', alpha=0.5, label='95% HPD Interval')
plt.xlabel("SPY Returns (Standardized)")
plt.ylabel("Portfolio Returns")
plt.legend()
plt.show()

# WAIC or LOO model comparison
waic = az.waic(idata)
loo = az.loo(idata)
print(waic)
print(loo)

# Interpretation and Reporting (Optional - You can add this part to summarize the findings)
print(f"Posterior Mean of Alpha: {summary.loc['alpha']['mean']}")
print(f"Posterior Mean of Beta: {summary.loc['beta']['mean']}")
print(f"Posterior Mean of Sigma: {summary.loc['sigma']['mean']}")
