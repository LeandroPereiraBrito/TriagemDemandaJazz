import pandas as pd
import re
import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def DataSet():
    dts = pd.read_csv("Contextualizacao.csv", sep=';', header=None, encoding="ISO-8859-1")
    return dts

def RemoverIrrelevantes(frase):
    frase = frase.lower()
    dicionario = nltk.corpus.stopwords.words('portuguese')
    palavra = [i for i in frase.split() if not i in dicionario]
    return (" ".join(palavra))

def RemoverAcentos(frase):
    fr = frase.lower()
    regex = "[^a-zA-Z0-9' ']"
    rt = re.sub(regex,'',fr)
    return rt


def Radical(frase):
    stemmer = nltk.stem.RSLPStemmer()
    palavra = []
    for i in frase.split():
        palavra.append(stemmer.stem(i))
    return (" ".join(palavra))



#Pré processamento
def Preprocess(frase):
    frase = RemoverIrrelevantes(frase)
    frase = RemoverAcentos(frase)
    frase = Radical(frase)
    return frase



def MachineLearning(termos,classfication,frase):
    vetor = CountVectorizer(analyzer="word")
    modelo = MultinomialNB()

    #vetorizar as frases
    freq_test = vetor.fit_transform(termos)
    freq_frase = vetor.transform(frase)

    #treinar o modelo
    modelo.fit(freq_test,classfication)
    return modelo.predict(freq_frase)








def Invoke(frase):
    # Preprocessar frase
    newFrase = Preprocess(frase)
    # Gerar data set de exemplos
    datSet = DataSet()
    termos = datSet[0]
    classificacao = datSet[1]
    # Preprocessar o data set
    newSet = [Preprocess(i) for i in termos]

    # retorna a  classificação da frase
    retorno = MachineLearning(newSet,classificacao,[newFrase])
    return retorno[0]





