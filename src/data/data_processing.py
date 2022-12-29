import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

from src.data.data_cleaning import select_features, fill_missing_values, seperate_city_data


def load_raw_data(train_feature_path, train_label_path, test_feature_path, test_results_path):
    """
    Load the raw data from the data directory
    :param train_feature_path: path to the training features
    :param train_label_path: path to the training labels
    :param test_feature_path: path to the test features
    :param test_results_path: path to the test results
    :return: tuple of dataframes (train_features, train_labels, test_features, test_results)
    """
    train_features = pd.read_csv(train_feature_path)
    train_labels = pd.read_csv(train_label_path)
    test_features = pd.read_csv(test_feature_path)
    test_submission = pd.read_csv(test_results_path)
    return train_features, train_labels, test_features, test_submission


def preprocess_data(data_path, labels_path=None):
    # load data and set index to city, year, weekofyear
    df = pd.read_csv(data_path, index_col=[0, 1, 2])

    # select features we want
    features = ['reanalysis_specific_humidity_g_per_kg',
                'reanalysis_dew_point_temp_k',
                'station_avg_temp_c',
                'station_min_temp_c']
    df = select_features(df, features)

    # fill missing values
    df = fill_missing_values(df)

    # add labels to dataframe
    if labels_path:
        labels = pd.read_csv(labels_path, index_col=[0, 1, 2])
        df = df.join(labels)

    # separate san juan and iquitos
    sj, iq = seperate_city_data(df)

    return sj, iq



def split_data(sj_train, iq_train):
    """
    Split the data into training and validation sets
    Since this is a timeseries model, we'll use a strict-future holdout set when we are splitting our train set
    :param sj_train: San Juan training data
    :param iq_train: Iquitos training data
    :return: tuple of dataframes (sj_train, sj_val, iq_train, iq_val)
    """
    sj_train_subtrain = sj_train.head(800)
    sj_train_subtest = sj_train.tail(sj_train.shape[0] - 800)

    iq_train_subtrain = iq_train.head(400)
    iq_train_subtest = iq_train.tail(iq_train.shape[0] - 400)
    return sj_train_subtrain, sj_train_subtest, iq_train_subtrain, iq_train_subtest


