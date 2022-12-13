import pandas as pd
from pandas import Series
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from utils import split_dataset_by_city, series_to_supervised

dataset = pd.read_csv('https://s3.amazonaws.com/drivendata/data/44/public/dengue_labels_train.csv', usecols=[3],
                      engine='python', skipfooter=3)
dataset1 = pd.read_csv('https://s3.amazonaws.com/drivendata/data/44/public/dengue_features_train.csv')
dataset2 = pd.read_csv('https://s3.amazonaws.com/drivendata/data/44/public/dengue_labels_train.csv')

iq, sj = split_dataset_by_city(dataset2)
iq = iq.drop(columns=['city', 'year', 'weekofyear'])
sj = sj.drop(columns=['city', 'year', 'weekofyear'])

dfall_iq, dfall_sj = split_dataset_by_city(dataset1)

dfall_iq = dfall_iq.drop(columns=['city', 'year', 'weekofyear', 'week_start_date'])
dfall_sj = dfall_sj.drop(columns=['city', 'year', 'weekofyear', 'week_start_date'])

dfall_iq['total_cases'] = Series(iq['total_cases'], index=dfall_iq.index)
dfall_sj['total_cases'] = Series(sj['total_cases'], index=dfall_iq.index)
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
dfall_iq.fillna(0, inplace=True)

values = dfall_iq.values
# integer encode direction
print(values[:, 20])
encoder = LabelEncoder()
values[:, 20] = encoder.fit_transform(values[:, 20])
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], axis=1,
              inplace=True)
print(type(reframed))

values = reframed.values
train = values
print(train.shape)

train_X, train_y = train[:, :-1], train[:, -1]
