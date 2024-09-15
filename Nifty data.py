import yfinance as yf 
import pandas as pd 
import openpyxl as op
start_date = "2019-01-01"
end_date = "2024-08-23"


closing_price = pd.DataFrame()
extracted_data = yf.download('^NSEI',start=start_date,end=end_date)
closing_price = extracted_data["Close"]
closing_price.to_excel(R"C:\Users\Ishaan Naolekar\Desktop\Nifty_data.xlsx")

data = pd.read_excel(R"C:\Users\Ishaan Naolekar\Desktop\Nifty_data.xlsx")
print(data)
