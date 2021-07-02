# Add some Library
import pandas as pd # For Dataframe/JSON processing 
import numpy as np # For Matrix operation
import nltk # Language Processing
from nltk.corpus import stopwords
nltk.download('stopwords') #Stopword
from nltk.tokenize import word_tokenize
import re # Regex
from gensim.parsing.preprocessing import STOPWORDS
nltk.download('punkt')

#Load the dataset from JSON file
df_review=pd.read_json('drive/MyDrive/soal-2.json')

#Create method for preprocessing text in 'KOMODITAS', to remove any stopword except the fish name.
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

#Create method for preprocessing text and number in 'BERAT', to remove any stopword except the fish weight number.
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

  fish_count={}
prepro_komoditas=prepo_komoditas(df_review['komoditas']
for i in range(len(df_review[:4])):
  for j in range(len(prepo_komoditas(df_review['komoditas'][i]))):
    for k in range(len(prepro_komoditas(df_review['komoditas'][i]))):
      if prepro_komoditas(df_review['komoditas'][i]) not in fish_count:
        fish_count[i]=df_review['komoditas'][i]

#Initialize for Preprocessing step in KOMODITAS
for i in range(len(df_review['komoditas'])):
  df_review['komoditas'][i]=prepro_komoditas(df_review['komoditas'][i])

df_review['komoditas']

#Initialize for Preprocessing step in BERAT
for i in range(len(df_review['berat'])):
  df_review['berat'][i]=prepro_berat(df_review['berat'][i])
