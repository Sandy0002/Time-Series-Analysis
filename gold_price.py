# In this program we will be estimating the gold prices and forecast future values
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
import matplotlib.pyplot as plt

data = pd.read_csv('gold_price_data.csv',parse_dates=[0])
print(data.head())

# Plotting gold prices
data['Value'].plot()

# Getting the trend of the gold rates
sns.regplot(x=data.index.values,y=data['Value'])
plt.show()

del data['Date']
# Train-Test split
trainSize = int(data.shape[0] * 0.8)
trainData =data[:trainSize]
testData = data[trainSize:]
# AR model creation
model = AutoReg(trainData,lags=2)
model = model.fit()

# Predicting for the next 15 days
size = len(data)
pred = model.predict(start=size,end=size+15)
print(pred)
