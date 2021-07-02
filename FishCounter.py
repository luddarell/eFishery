import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import re
from gensim.parsing.preprocessing import STOPWORDS
nltk.download('punkt')

df_review=pd.read_json('drive/MyDrive/soal-2.json')

def prepro_komoditas(komoditas):
  all_stopwords_gensim = STOPWORDS.union(set(['ikan']))
  text = komoditas
  text_tokens = word_tokenize(text)
  #print(text_tokens)
  tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
  #print(tokens_without_sw)
  if ',' in tokens_without_sw:
    token=[s for s in tokens_without_sw if s != ',']
    return token
  else:
    return tokens_without_sw

def prepro_berat(berat):
  all_stopwords_gensim = STOPWORDS.union(set(['ikan','lele','bawal','nila','pindang tongkol','gurame','mas','mujaer','kembung','salem','rata2','rata rata','rata','sampe','kurang','-','gak nentu','kadang','s.d']))
  text = berat
  text_tokens = word_tokenize(text)
  tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
  test_list = tokens_without_sw
  unit = "kg"
  res = re.findall('\d+', ' '.join(test_list))
  for i in range(0, len(res)):
    res[i] = int(res[i])
  return res