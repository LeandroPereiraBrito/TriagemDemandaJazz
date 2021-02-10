import spacy
from nltk import FreqDist as freq

def RetornaNucleo(parametro):
    #Instancia a linhgua
    nlp = spacy.load("pt")

    #submeter a frase ao spacy
    doc = nlp(parametro)

    # Gerar o dataSet com as dependencia das palavras
    dep_labels = []
    for token in doc:
        while token.head != token:
            x = token.text
            dep_labels.append(x)
            token = token.head

    # Pegar a frequencia de mandatoria de palavaras
    maiorFreq = freq(item for item in dep_labels)
    mf1 = maiorFreq.most_common(1)

    print(mf1)

    return parametro