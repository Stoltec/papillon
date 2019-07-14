import os.path

import pandas as pd

def load_data(force_rebuild = False):
    if (force_rebuild == True or os.path.exists('data/dataset.csv') == False):
        return build_dataset()

    return pd.read_csv('data/dataset.csv')

def build_dataset():
    dataset = None

    for x in range(1, 4):
        tmp = pd.read_csv('data/articles' + str(x) + '.csv', 
        delimiter=',').loc[:, 'content']

        if (dataset is None):
            dataset = tmp
        else:
            dataset = pd.concat([dataset, tmp], ignore_index = True)
    dataset.columns = ['', 'content']
    dataset.to_csv('data/dataset.csv', mode = 'a', header = True, index = False)
    return dataset
