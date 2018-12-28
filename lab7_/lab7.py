import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': ['w', 'x', 'y', 'z']})
print(df)
print(df.info())

log_df = pd.read_csv('./wc_day6_1_sample.csv',
                     names=['ClientID', 'Date', 'Time', 'URL', 'ResponseCode', 'Size'],
                     na_values='-',
                     encoding='ansi')
