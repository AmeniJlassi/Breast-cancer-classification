# import the necessary packages
import os
# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "datasets/orig"
# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "datasets/idc"
# derive the training, validation, and testing directories
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])
# define the amount of data that will be used training
#the percentage of data that will be used for training. Here I’ve set it to 80%, where the remaining 20% will be used for testing.
TRAIN_SPLIT = 0.8
# 10% of the training data (after we’ve split off the testing data) will be used for validation.
VAL_SPLIT = 0.1
