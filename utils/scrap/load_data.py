import os.path

import pandas as pd

def load_data_news(force_rebuild = False):
    if (force_rebuild == True or os.path.exists('data/dataset.csv') == False):
        return build_news()

    return pd.read_csv('data/dataset.csv')

def build_news():
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

def load_data_recipes(force_rebuild = False):
    if (force_rebuild == True or os.path.exists('data/food/dataset.csv') == False):
        return build_food()

    return pd.read_csv('data/food/food_dataset.csv')

def build_food():
    dataset = None

    dataset = pd.read_csv('data/food/clean_recipes.csv', 
    delimiter=';').loc[:, 'Directions']

    dataset.columns = ['', 'Directions']
    dataset.to_csv('data/food/dataset.csv', mode = 'a', header = True, index = False)
    return dataset
