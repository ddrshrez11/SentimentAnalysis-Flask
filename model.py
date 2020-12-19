import pickle
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.ensemble import RandomForestClassifier



# load ML Vectorizer
with open('models/vect_pickle','rb') as f:
    vectorizer=pickle.load(f)
#load Naive Bayes Classifier
with open('models/nb_pickle','rb') as f:
    nb=pickle.load(f)
#load Random Forest Classifier
with open('models/rfc_pickle','rb') as f:
    rfc=pickle.load(f)

# load LSTM Vectorizer
with open('models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
# #load LTSM Model
# loaded_model=keras.models.load_model(".\models\\")
loaded_model=load_model('models/ltsm.h5')

predictions={}
prediction_label=['negative','postitive']


def model_run(tweet_data):
    replies=tweet_data.get('replies')
    #---------------LSTM model------------------------
    tweets = replies
    tweets = tokenizer.texts_to_sequences(tweets)
    tweets = pad_sequences(tweets,maxlen=200)
    p_lstm = loaded_model.predict_classes(tweets)
    p=p_lstm.transpose().tolist()
    
    #array of predictions
    pred_arr= p[0]
    predictions['lstm']=pred_arr
    #print(pred_arr)

    #--------------------------------------------------


    #------------------NB model------------------------
    #tweet_replies_content=np.array(['fake news','he is a good boy.'])
    tweet_replies_vector= vectorizer.transform(replies)
    p_nb = nb.predict(tweet_replies_vector)
    pred_nb=p_nb.transpose().tolist()
    pred_nb = [1 if x==4 else x for x in pred_nb]
    #print(pred_nb)
    predictions['nb']=pred_nb

    #--------------------------------------------------


    #------------------RF model------------------------
    p_rfc=rfc.predict(tweet_replies_vector)
    pred_rfc=p_rfc.transpose().tolist()
    pred_rfc = [1 if x==4 else x for x in pred_rfc]
    #print(pred_rfc)
    predictions['rfc']=pred_rfc
    #--------------------------------------------------
    print(predictions)
    return predictions

#print(model_run(['fake news','he is a good boy']))