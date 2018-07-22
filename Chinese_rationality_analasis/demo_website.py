from os import listdir
from os.path import isfile, join
import jieba
import codecs
# convert Traditional Chinese characters to Simplified Chinese characters
from langconv import *
import pickle
import random

import numpy as np
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import GRU
from keras.preprocessing.text import Tokenizer
from keras.layers.core import Dense
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import TensorBoard


def __pickleStuff(filename, stuff):
    save_stuff = open(filename, "wb")
    pickle.dump(stuff, save_stuff)
    save_stuff.close()


def __loadStuff(filename):
    saved_stuff = open(filename, "rb")
    stuff = pickle.load(saved_stuff)
    saved_stuff.close()
    return stuff


model = None
sentiment_tag = None
maxLength = None


def loadModel():
    global model, sentiment_tag, maxLength
    metaData = __loadStuff("./Data/meta_sentiment_chinese.p")
    maxLength = metaData.get("maxLength")
    vocab_size = metaData.get("vocab_size")
    output_dimen = metaData.get("output_dimen")
    sentiment_tag = metaData.get("sentiment_tag")
    embedding_dim = 256
    if model is None:
        model = Sequential()
        model.add(Embedding(vocab_size, embedding_dim, input_length=maxLength))
        # Each input would have a size of (maxLength x 256) and each of these 256 sized vectors are fed into the GRU layer one at a time.
        # All the intermediate outputs are collected and then passed on to the second GRU layer.
        model.add(GRU(256, dropout=0.9, return_sequences=True))
        # Using the intermediate outputs, we pass them to another GRU layer and collect the final output only this time
        model.add(GRU(256, dropout=0.9))
        # The output is then sent to a fully connected layer that would give us our final output_dim classes
        model.add(Dense(output_dimen, activation='softmax'))
        # We use the adam optimizer instead of standard SGD since it converges much faster
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])
        model.load_weights('./Data/sentiment_chinese_model.HDF5')
        model.summary()
    print("Model weights loaded!")


def findFeatures(text):
    text = Converter('zh-hans').convert(text)
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    seg_list = jieba.cut(text, cut_all=False)
    seg_list = list(seg_list)
    text = " ".join(seg_list)
    textArray = [text]
    input_tokenizer_load = __loadStuff("./Data/input_tokenizer_chinese.p")
    textArray = np.array(pad_sequences(
        input_tokenizer_load.texts_to_sequences(textArray), maxlen=maxLength))
    return textArray


def predictResult(text):
    if model is None:
        print("Please run \"loadModel\" first.")
        return None
    features = findFeatures(text)
    # we have only one sentence to predict, so take index 0
    predicted = model.predict(features)[0]
    predicted = np.array(predicted)
    probab = predicted.max()
    predition = sentiment_tag[predicted.argmax()]
    return predition, probab


loadModel()

from auto_everything.web import Selenium
while 1:
    url = input("请输入你想要分析的网站url: ")
    if url.strip('\n ') == "":
        continue

    my_selenium = Selenium(url)
    driver = my_selenium.driver

    elements = my_selenium.wait_until_exists('//p')

    for e in elements:
        try:
            text = e.text.strip('\n ')
            if text != "":
                r = predictResult(text)
                print(text[:100], '\n', r, '\n'*2)
        except Exception as e:
            pass

    driver.close()
