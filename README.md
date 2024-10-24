# Black-Scholes Option Pricing and Implied Volatility Calculator


## Overview


https://github.com/user-attachments/assets/9375eb28-1448-4fbf-900b-bfcde3d1fac8


This project is an interactive web application built with Streamlit that implements the Black-Scholes model for option pricing and implied volatility calculation. It provides a user-friendly interface for financial analysts, students, and professionals to quickly compute option prices and implied volatilities.

## Features

- Calculate option prices using the Black-Scholes model
- Compute implied volatility for given market option prices
- Support for both call and put options
- Interactive user interface for inputting option parameters
- Real-time calculations and result display

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/black-scholes-calculator.git
   ```

2. Navigate to the project directory:
   ```
   cd black-scholes-calculator
   ```

3. Install the required dependencies:
   ```
   pip install streamlit numpy scipy matplotlib
   ```

## Usage

Run the Streamlit app:
streamlit run app.py


Then, open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

## Theory

### The Black-Scholes Model

The Black-Scholes model, developed by Fischer Black, Myron Scholes, and Robert Merton in 1973, is a mathematical model for pricing European-style options. The model assumes that the price of heavily traded assets follows a geometric Brownian motion with constant drift and volatility.

Key assumptions of the Black-Scholes model:
1. The stock price follows a lognormal distribution.
2. There are no transaction costs or taxes.
3. The risk-free interest rate is constant.
4. The stock does not pay a dividend.
5. There is no arbitrage opportunity.

### Black-Scholes Formula

For a European call option, the Black-Scholes formula is:

C = S₀N(d₁) - Ke^(-rT)N(d₂)

Where:
- C is the call option price
- S₀ is the current stock price
- K is the strike price
- r is the risk-free interest rate
- T is the time to maturity
- N(x) is the cumulative distribution function of the standard normal distribution
- d₁ = (ln(S₀/K) + (r + σ²/2)T) / (σ√T)
- d₂ = d₁ - σ√T
- σ is the volatility of the underlying asset

For a European put option, the formula is:

P = Ke^(-rT)N(-d₂) - S₀N(-d₁)

### Implied Volatility

Implied volatility is the market's forecast of a likely movement in a security's price. It is a metric used to estimate future fluctuations (volatility) of a security's price based on certain predictive factors.

In the context of the Black-Scholes model, implied volatility is the value of σ (volatility) that, when input into the Black-Scholes formula, gives a theoretical option price equal to the current market price of that option.

This project uses the Newton-Raphson method to iteratively solve for the implied volatility given the market price of an option and other known parameters.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
