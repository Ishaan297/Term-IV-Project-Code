import pandas as pd
import numpy as np
from arch import arch_model
import matplotlib.pyplot as plt


file_path = R"C:\Users\Ishaan Naolekar\Desktop\TATA_MOTORS.xlsx"  
df = pd.read_excel(file_path)

df['Date'] = pd.to_datetime(df['Date'])  # Convert date column to datetime
df.set_index('Date', inplace=True)


df['Close'] = np.log(df['Close'] / df['Close'].shift(1)) * 100  # Rescale by multiplying log returns by 100
df['CNX Close'] = np.log(df['CNX Close'] / df['CNX Close'].shift(1)) * 100  # Rescale by multiplying log returns by 100


df.dropna(inplace=True)


garch_model = arch_model(df['Close'], vol='Garch', p=1, q=1)
garch_result = garch_model.fit()


print(garch_result.summary())

# Step 5: Forecast future volatility
forecast = garch_result.forecast(horizon=5)  # 5 days forecast
print(forecast.variance[-1:])  # Print variance forecast

# Step 6: Plotting the volatility from the GARCH model
plt.figure(figsize=(10, 6))
plt.plot(df.index, garch_result.conditional_volatility, label='Conditional Volatility (Tata Motors)', color='blue')
plt.title('GARCH(1,1) Model - Tata Motors Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# Step 7: Apply GARCH to Nifty Auto for comparison
garch_model_nifty = arch_model(df['CNX Close'], vol='Garch', p=1, q=1)
garch_result_nifty = garch_model_nifty.fit()

# Print the summary for Nifty Auto
print(garch_result_nifty.summary())

# Step 8: Plotting Nifty Auto Volatility
plt.figure(figsize=(10, 6))
plt.plot(df.index, garch_result_nifty.conditional_volatility, label='Conditional Volatility (Nifty Auto)', color='red')
plt.title('GARCH(1,1) Model - Nifty Auto Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()
