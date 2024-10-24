import streamlit as st
import numpy as np
import scipy.stats as st_stats

def dV_dsigma(S_0, K, sigma, tau, r):
    d2 = (np.log(S_0 / K) + (r - 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    return K * np.exp(-r * tau) * st_stats.norm.pdf(d2) * np.sqrt(tau)

def BS_Call_Option_Price(CP, S_0, K, sigma, tau, r):
    d1 = (np.log(S_0 / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if CP.lower() in ["c", "1"]:
        return st_stats.norm.cdf(d1) * S_0 - st_stats.norm.cdf(d2) * K * np.exp(-r * tau)
    elif CP.lower() in ["p", "-1"]:
        return st_stats.norm.cdf(-d2) * K * np.exp(-r * tau) - st_stats.norm.cdf(-d1) * S_0

def ImpliedVolatility(CP, S_0, K, sigma, tau, r, V_market):
    optPrice = lambda s: BS_Call_Option_Price(CP, S_0, K, s, tau, r)
    vega = lambda s: dV_dsigma(S_0, K, s, tau, r)
    
    error = 1e10
    n = 1
    max_iterations = 100
    while error > 1e-10 and n < max_iterations:
        g = optPrice(sigma) - V_market
        g_prim = vega(sigma)
        sigma_new = sigma - g / g_prim
        error = abs(g)
        sigma = sigma_new
        n += 1
    
    return sigma, n

st.title("Black-Scholes Implied Volatility Calculator")

S_0 = st.number_input("Current Stock Price (S_0)", value=100.0, step=0.01)
K = st.number_input("Strike Price (K)", value=120.0, step=0.01)
r = st.number_input("Risk-free Rate (r)", value=0.05, step=0.01)
tau = st.number_input("Time to Maturity (tau, in years)", value=1.0, step=0.01, min_value=0.01)
V_market = st.number_input("Market Option Price", value=2.0, step=0.01)
CP = st.selectbox("Option Type", ["c", "p"], format_func=lambda x: "Call" if x == "c" else "Put")
sigma_init = st.number_input("Initial Volatility Guess", value=0.25, step=0.01)

if st.button("Calculate Implied Volatility"):
    try:
        sigma_imp, iterations = ImpliedVolatility(CP, S_0, K, sigma_init, tau, r, V_market)
        
        st.success(f"Implied Volatility: {sigma_imp:.7f}")
        st.info(f"Number of iterations: {iterations}")
        
        message = f"""Implied volatility for:
        Option Type = {"Call" if CP == "c" else "Put"}
        Option Price = ${V_market:.2f}
        Strike (K) = ${K:.2f}
        Maturity (tau) = {tau:.2f} years
        Interest Rate (r) = {r:.2%}
        Initial Stock Price (S_0) = ${S_0:.2f}
        
        Equals to sigma_imp = {sigma_imp:.7f}"""
        
        st.write(message)
        
        # Verification
        val = BS_Call_Option_Price(CP, S_0, K, sigma_imp, tau, r)
        st.write(f"Verification: Option Price for implied volatility of {sigma_imp:.7f} is equal to ${val:.7f}")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Unable to calculate implied volatility. Please check your inputs and try again.")