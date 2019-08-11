import logging
import os.path
import sys

#from utils.load_data import load_data
#from utils.sanitize_corpus import sanitize_data
from utils.gensim_word2vec import build_word2vec



program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
     
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))

word2vec = build_word2vec('default_sanitized.csv')

print(word2vec.most_similar('crime'))
