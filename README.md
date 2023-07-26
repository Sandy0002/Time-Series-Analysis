# Time Series Forecasting

Repository consists of programs that use various concepts and models used for time series forecasting.

## Contents
+ [About](#intro) 
+ [Applications](#applications) 
+ [Terms](#terms) 
+ [Datasets Description](#data)
+ [Libraries Used](#library)
+ [Programs Description](#program)
+ [LICENSE](LICENSE)


<a id="intro"></a><h2>About</h2>

Time series analysis is a statistical and data analysis technique used to analyze and model time-ordered data. Time series is one of the most common used technique in day to day life. Its application ranges from **stock required for an inventory** to **stock price prediction on stock exchange.** In this repository few of such applications such as arms imported is estimated, temperature variance estimation etc have been worked out. To learn more about [here](#data)

<a id="applications"></a><h2>Applications</h2>
There are a wide range of applications of time series forecasting few are mentioned below:

+ Financial Forecasting
+ Demand Forecasting
+ Energy Consumption Prediction
+ Weather Forecasting
+ Sales and Economic Forecasting
+ Healthcare and Medical Forecasting

<a id="terms"></a><h2>Terms</h2>
To get started with the time series analysis and forecasting we need to have knowledege about several terms used.The terms and their meaning are described below:

| TERMS        | MEANING       
| ------------- |:-------------:|
| **Time Series** | A sequence of data points ordered in time at regular intervals.|
| **Trend** | The long-term movement or direction in a time series.
| **Seasonality** | A repeating pattern or cycle in a time series that occurs at fixed intervals, often corresponding to seasons.|
| **Stationarity** | A time series is said to be stationary if its statistical properties (mean, variance, and autocorrelation) do not change over time.|
| **Lag** |  The time difference between a data point and its corresponding observation in the past. |
| **Seasonal Decomposition** | The process of breaking down a time series into its trend, seasonality, and residual components.|
| **Autocorrelation(ACF)** | The correlation of a time series with its own lagged values. It measures how previous observations relate to the current observation. |
| **Partial Autocorrelation (PACF)** | The correlation between two time series observations, accounting for the influence of other time lags.|
| **Moving Average (MA)** | A time series model that uses past error terms as input to predict future values. |
| **Autoregression (AR)** | A is a method used to model that uses past observations of the time series itself as input to predict future values.|



<a id="data"></a><h2>Datasets Description</h2>
The datasets used for the programs are downloaded from **kaggle**.And they can be found [here](https://github.com/Sandy0002/Time-Series-Analysis/tree/main/Datasets)


Dataset Name      | Description
| ------------- |:-------------:|
**AAPL_2006-01-01_to_2018-01-01** | This dataset consists of stock price of apple taken from January 2006 to January 2018
**Arms Imports Per Country(1950-2020)** | This dataset consists of arms imports of several countries from 1950 to 2020.
**Delhi Weather** | This dataset consists of weather details of Delhi which consists of columns such as temperature, humidity, wind speed and mean value of pressure of the air
**Energy Required** | This dataset encompasses energy being consumed by various states of India and total consumption in India.
**Gold Prices** | The most opted metal on the planet i.e **Gold** its price values is present in this dataset.

<a id="library"></a><h2>Libraries Used</h2>
+ **Numpy** : Used for numerical computations in python
+ **Pandas** : Used for file reading and other operations when working with large data.
+ **Sklearn(Scikit-learn)** : This is a machine learning library for python.
+ **Matplotlib** : Visualization library
+ **Seaborn** : Interactive visualizations are made using these library.
+ **Statsmodels** : This is library is used purely for statistical purposes.

<a id="program"></a><h2>Programs Description</h2>

Before moving ahead with the description the most fundemental things to know in the time series analysis is that one needs to have right data and enough amount of data to get started. The data needs to be cleaned and treated. If necessary then normalization and dimensionality scaling all these methods are needed to be done. Apart from the general stuff in here we need to **check if there is a trend and seasonality in the data**. As if we are to infer some information from the data then we need to deal with this two. As if these are present then it may mislead our results.

The programs that are describe here in a sequential manner showing from Auto Regression model to SARIMAX model.

Program Name      | Description
| ------------- |:-------------:|
**Gold Prices** | Here we have used gold_prices dataset in that there is only two columns one is the time series and other is price of the gold that varied from 1970 to 2020. Since we have only gold price so an Auto Regression model is used which is used for forecasting data from available past data. Program [link](https://github.com/Sandy0002/Time-Series-Analysis/blob/main/gold_price.py)
**Gold Prices with ARMA model**| After the auto regression in order to improve performance further the ARMA model is used as it uses both Auto Regression and Moving Average into the account which leads a better performance generally.Program [link](https://github.com/Sandy0002/Time-Series-Analysis/blob/main/gold_price_arma.py)
**Arms Imports** | This program uses arms_import data in that India's arms imports have been chosen here. The program uses ARIMA model so that data non-stationary data can be brought down to stationary state by differencing.**ARIMA stands for Auto Regression(AR)  Integration(I)  MOVING AVERAGE(MA)** ARIMA model is preferred when there is no seasonality to remove trend from the data.Program [link](https://github.com/Sandy0002/Time-Series-Analysis/blob/main/arms_imports.py)
**Energy Requirements** | This program uses energy_req dataset. In that dataset various columns consisting of time series, states of India and total Indian consumption of energy is present. For our purpose total consumption of India has been chosen. As energy consumption is seasonal hence demonstration of **SARIMA i.e Seasonal ARIMA** have been used.Program [here](https://github.com/Sandy0002/Time-Series-Analysis/blob/main/energy_requirements.py)
**Delhi Temperature** | This program uses delhi weather dataset which consists of temperature,mean pressure, wind speed and humidity.In this program we are estimating the temperature of the data and since other than temperature we have other variables such as humidity, wind speed and pressure so we **SARIMAX** model is used which is used to apply data having seasonal data and consists of exogeneous variables.Program [here](https://github.com/Sandy0002/Time-Series-Analysis/blob/main/delhi_temperature.py)


## LICENSE
[MIT LICENSE](LICENSE)
