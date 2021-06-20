import pandas as pd
from dateutil import parser


df = pd.read_csv(r"F:\leap_lstm\123_20200101_20200401.csv")

dates = df['DateKey'].unique()
# print(dates)
date_times = []
for i,row in df.iterrows():

    if (len(str(row['TimeKey'])) < 6):
        prefix = '0' * (6 - len(str(row['TimeKey'])))
        time_st = prefix + str(row['TimeKey'])
    else:
        time_st = str(row['TimeKey'])


    date_time = parser.parse(str(row['DateKey'])+' '+time_st)
    date_times.append(date_time)

    # print(date_time)
df['timestamp'] = date_times



df = df.sort_values(['timestamp'], ascending=True)

# print(df.head(200))

df.to_csv('processed_123_20200101_20200401.csv')

