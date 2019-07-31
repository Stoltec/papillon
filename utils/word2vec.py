from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

def build_word2vec(input_file):
    try:
        nltk.download('stopwords')
    except:
        pass

    sentences = list(read_file(input_file))
    model = Word2Vec(sentences, size = 150, window = 8, min_count = 10, workers = 8)
    model.train(sentences, total_examples = len(sentences), epochs = 16)

    return model

def read_file(input_file):
    with open(input_file, 'rb') as in_file:
        for line in (in_file):
            # remove all accents and words of less than three letters
            yield simple_preprocess(line, deacc = True, min_length = 3)


