import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

file_path = 'path_to_your_excel_file.xlsx'
data = pd.read_excel(R"C:\Users\Ishaan Naolekar\Desktop\INDIA VIX DATA.xlsx")
print(data.head())

# Independent variable (India VIX)
X = data[['VIX']].values

# Dependent variable (Nifty 50)
y = data['NIFTY50'].values

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)
plt.scatter(data['VIX'], y, color='blue', label='Original Data')
plt.plot(data['VIX'], y_pred, color='red', label='Fitted Curve')
plt.xlabel('India VIX Closing Price')
plt.ylabel('Nifty 50 Closing Price')
plt.title('Nonlinear Relationship: India VIX vs Nifty 50')
plt.legend()
plt.show()



