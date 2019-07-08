def read_data():
    articles = pd.read_csv('data/articles2.csv', delimiter=',').loc[:, 'content']
    for x in range(2, 4):
        tmp = pd.read_csv('data/articles' + str(x) + '.csv', delimiter=',').loc[:, 'content']
        articles = pd.concat([articles, tmp])
    #articles.to_csv('data/dataset.csv', mode = 'a', header = False)
    return articles
