import pandas as pd

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

correlation = pd.DataFrame()
for id in train_data.columns[1:-2]:
    for dv in train_data.columns[-2:]:
        correlation.loc[id, dv] = train_data[id].corr(train_data[dv])

print(train_data.tail())
print(test_data.head())