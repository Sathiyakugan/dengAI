import os

DATA_PATH_RAW = os.path.join("..", "data", "raw")

TRAIN_FEATURE_FILE = 'DengAI_Predicting_Disease_Spread_-_Training_Data_Features.csv'
TRAIN_LABEL_FILE = 'DengAI_Predicting_Disease_Spread_-_Training_Data_Labels.csv'
TEST_FEATURE_FILE = 'DengAI_Predicting_Disease_Spread_-_Test_Data_Features.csv'
TEST_RESULTS_FILE = 'DengAI_Predicting_Disease_Spread_-_Submission_Format.csv'

TRAIN_FEATURE_PATH_RAW = os.path.join(DATA_PATH_RAW, TRAIN_FEATURE_FILE)
TRAIN_LABEL_PATH_RAW = os.path.join(DATA_PATH_RAW, TRAIN_LABEL_FILE)
TEST_FEATURE_PATH_RAW = os.path.join(DATA_PATH_RAW, TEST_FEATURE_FILE)
TEST_RESULTS_PATH_RAW = os.path.join(DATA_PATH_RAW, TEST_RESULTS_FILE)

DATA_PATH_PROCESSED = os.path.join("..", "data", "processed")
TRAIN_FEATURE_PATH_PROCESSED= os.path.join(DATA_PATH_PROCESSED, TRAIN_FEATURE_FILE)
TRAIN_LABEL_PATH_PROCESSED = os.path.join(DATA_PATH_PROCESSED, TRAIN_LABEL_FILE)
TEST_FEATURE_PATH_PROCESSED = os.path.join(DATA_PATH_PROCESSED, TEST_FEATURE_FILE)
TEST_RESULTS_PATH_PROCESSED = os.path.join(DATA_PATH_PROCESSED, TEST_RESULTS_FILE)

MODEL_PATH = os.path.join("..", "models")
SJ_BEST_MODEL_PATH = os.path.join(MODEL_PATH, "sj_best_model.pkl")
IQ_BEST_MODEL_PATH = os.path.join(MODEL_PATH, "iq_best_model.pkl")

