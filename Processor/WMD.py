# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:07:15 2020

@author: Ratan Singh
"""

from word_mover_distance import model

from Processor.Processor import Processor
from Embeddings.Glove import Glove

class WMD(Processor):

    def __init__(self):
        self.__model = None
        self.__text1 = ""
        self.__text2 = ""
        self.__tokenEmbedding1 = None
        self.__tokenEmbedding2 = None
        self.__distanceMatrix = None
        self.__matrix = None
        self.__d1 = None
        self.__d2 = None

    def load(self):
        glove = Glove()
        wmdmodel = glove.load()
        return wmdmodel

    def getWMDResponse(self, wmdmodel, query, selected_titles, selected_titles_len):
        wmdresponse = []
        for i in range(selected_titles_len):
            s1 = query.lower().split()
            s2 = selected_titles[i].lower().split()
            wmdresponse.append(wmdmodel.wmdistance(s1, s2))
        return wmdresponse

    '''
    def read_data(file_name):
        with open(file_name, 'r') as f:
            word_vocab = set()  # not using list to avoid duplicate entry
            word2vector = {}
            for line in f:
                line_ = line.strip()  # Remove white space
                words_Vec = line_.split()
                word_vocab.add(words_Vec[0])
                word2vector[words_Vec[0]] = np.array(words_Vec[1:], dtype=float)
        print("Total Words in DataSet:", len(word_vocab))
        return word_vocab, word2vector

    def cos_sim(u, v):
        """
        u: vector of 1st word
        v: vector of 2nd Word
        """
        numerator_ = u.dot(v)
        denominator_ = np.sqrt(np.sum(np.square(u))) * np.sqrt(np.sum(np.square(v)))
        return numerator_ / denominator_


    def transform(self):
        pass

    def predict(self, text1, text2):
        #self.__text1, self.__text2 = text1, text2
        #model = model.WordEmbedding(model_fn="F://OFFICIAL//SMART PDF ASSISTANT//Smart-pdf-assistant//ThirdPartyData//glove.6B//glove.6B.50d.txt")
        s1 = text1.lower().split()
        s2 = text2.lower().split()
        wmdistance = model.wmdistance(s1, s2)

        return wmdistance

    def __computeTokenEmbeddings(self):
        tokens1 = word_tokenize(self.__text1)
        tokens2 = word_tokenize(self.__text2)

        self.__tokenEmbedding1 = self.__model.predict(tokens1)
        self.__tokenEmbedding2 = self.__model.predict(tokens2)

    def __computeDistanceMatrix(self):
        docset1 = np.array(pd.DataFrame(self.__tokenEmbedding1).drop_duplicates())
        docset2 = np.array(pd.DataFrame(self.__tokenEmbedding2).drop_duplicates())

        matrix = np.array(pd.DataFrame(docset1).append(pd.DataFrame(docset2)).drop_duplicates())
        vocab_len = matrix.shape[0]

        distance_matrix = np.zeros([vocab_len, vocab_len])
        for i in range(vocab_len):
            for j in range(vocab_len):
                condition1 = np.array([(np.array(docset1)[k, :] == matrix[i, :]).all() for k in range(docset1.shape[0])]).any()
                condition2 = np.array([(np.array(docset2)[k, :] == matrix[j, :]).all() for k in range(docset2.shape[0])]).any()
                if not condition1 or not condition2:
                    continue
                distance_matrix[i, j] = np.linalg.norm(matrix[i, :] - matrix[j, :])

        self.__matrix = matrix
        self.__distanceMatrix = distance_matrix

    def __computeNBOW(self, tokenEmb):
        matrix = self.__matrix
        tokenEmb = np.array(tokenEmb)
        nbowCount = np.array([np.sum(np.array([(np.array(tokenEmb)[k, :] == matrix[i, :]).all() for k in range(tokenEmb.shape[0])]) * 1.0) for i in range(matrix.shape[0])])
        return nbowCount / np.sum(nbowCount)

    def __emdDistance(self):
        self.__computeTokenEmbeddings()
        self.__computeDistanceMatrix()

        self.__d1 = self.__computeNBOW(self.__tokenEmbedding1)
        self.__d2 = self.__computeNBOW(self.__tokenEmbedding2)

        return emd(self.__d1, self.__d2, self.__distanceMatrix)'''
