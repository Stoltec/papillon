import csv, os, random
import numpy as np

DATA_DIR = 'data/food/recipes'

# perform randomized splitting and sentence length padding
def load_and_split(random_pad = True, find_sentence_length = True,
        max_sentence_length = 20, train = 0.7, valid = 0.15, test = 0.15):
    # Make sure the split sizes sum to 1
    if (train + test + valid != 1.0):
        raise Exception('train_size + test_size + valid_size != 1.0')

    # find information about the dataset so we can make our numpy array
    sentence_length, vector_size, num_datapoints = get_dataset_info()

    # hard-set the maximum sentence length
    if (not find_sentence_length):
        sentence_length = max_sentence_length

    # read in the data from files
    data, labels = read_then_pad(random_pad, num_datapoints,
            sentence_length, vector_size)

    # split the dataset accordingly
    #train, valid, test = split(data, labels, train, valid, test)

    return data, labels
    return train_set, valid_set, test_set

def get_dataset_info():
    # max sentence length found so far
    max_length = 0
    # length of the current sentence
    tmp_length = 0
    # number of sentences
    num_datapoints = 0
    # length of the word emedding vector
    vector_size = 0

    # read DATA_DIR/0/0_embedded.csv to get the embedding vector size
    with open(DATA_DIR + '/0/0_embedded.csv', 'r') as c:
        # assumes all rows don't have a trailing ',' after the last element
        vector_size = c.readline().count(',')

    for d in os.listdir(DATA_DIR):
        # if it is a directory
        if (os.path.isdir(os.path.join(DATA_DIR + '/' + d))):
            for f in os.listdir(DATA_DIR + '/' + d):
                # if it is a file is a .csv (ignores the .txt of the sentence)
                if (os.path.isfile(os.path.join(DATA_DIR + '/' + d + '/' + f))
                        and f.endswith('_embedded.csv')):
                    # count the lines in the file and update max
                    with open(DATA_DIR + '/' + d + '/' + f, 'r') as csv_file:
                        tmp_length = sum(1 for line in csv_file)
                        if (tmp_length > max_length):
                            max_length = tmp_length
                    # increment the total number of sentences
                    num_datapoints += 1
                    tmp_length = 0

    return max_length, vector_size, num_datapoints

# TODO: add in the random padding
def read_then_pad(random_pad, num_datapoints, sentence_len, vector_size):
    data = np.zeros((num_datapoints, sentence_len * vector_size),
            dtype = np.float)
    labels = np.zeros((num_datapoints, sentence_len), dtype = np.float)

    point_index = 0

    for d in os.listdir(DATA_DIR):
        # if it is a directory
        if (os.path.isdir(os.path.join(DATA_DIR + '/' + d))):
            for f in os.listdir(DATA_DIR + '/' + d):
                # if it is a file is a .csv (ignores the .txt of the sentence)
                if (os.path.isfile(os.path.join(DATA_DIR + '/' + d + '/' + f))
                        and f.endswith('_embedded.csv')):
                    # read the whole .csv
                    with open(DATA_DIR + '/' + d + '/' + f, 'r') as csv_file:
                        # offset for random pad
                        off = 0
                        # if random pad is enabled
                        if (random_pad):
                            # find the current sentence length
                            curr_len = sum(1 for line in csv_file)
                            # random offset ensuring that the sentence sill fits
                            off = random.randint(0, sentence_len - curr_len)

                    with open(DATA_DIR + '/' + d + '/' + f, 'r') as csv_file:
                        reader = csv.reader(csv_file)
                        # iterate over the rows
                        for r, row in enumerate(reader):
                            for e, element in enumerate(row):
                                # if it is data
                                if (e < (len(row) - 1)):
                                    data[point_index][((r + off) * vector_size) + e] = element
                                # if it is a label
                                else:
                                    labels[point_index][r + off] = element
                    # increment the index for a datapoint
                    point_index += 1

    return data, labels
