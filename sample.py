import pandas as pd
names=["ticker", "date","open", "high", "low", "close","volumne","ex-dividend","split-ratio","adj_open","adj_high","adj_low","adj_close", "adj_volume"]
url = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?api_key=PVQQi6AQh7YiszjYePw_"
df = pd.read_csv(url, names=names)
df = df[['adj_open', 'adj_high','adj_low', 'adj_close','adj_volume',]]
df['HL_PCT'] = (df['adj_high'] - df['adj_close']) / df['adj_close'] 
df['PCT_change'] = (df['adj_close'] - df['adj_open']) / df['adj_open']
df = df[['adj_close','HL_PCT','PCT_change', 'adj_volume']]
print(df.describe())