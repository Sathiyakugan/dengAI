# fill missing values method
def fill_missing_values(df):
    df.fillna(method='ffill', inplace=True)
    return df

# select features
def select_features(df, columns):
    df = df[columns]
    return df

# seperate san juan and iquitos
def seperate_city_data(df):
    sj = df.loc['sj']
    iq = df.loc['iq']
    return sj, iq


