# hedge_pricing.py
import numpy as np
from scipy.stats import norm

def black_scholes_put_price(S, K, T, r, sigma):
    """
    Compute the Black-Scholes price of a European put option.
    
    Parameters:
      S : float - current price of the underlying
      K : float - strike price
      T : float - time to maturity in years
      r : float - risk-free interest rate
      sigma : float - annualized volatility
      
    Returns:
      put_price : float - price of the put option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

if __name__ == '__main__':
    S = 100      
    K = 90       
    T = 0.25     
    r = 0.01     
    sigma = 0.2  
    
    price = black_scholes_put_price(S, K, T, r, sigma)
    print("Black-Scholes put price:", price)
