import spacy
from nltk import FreqDist
import principal

def RetornNucleo(frase):
    # Instancia a spacy no modelo portugues
    nlp = spacy.load("pt")

    # submeter a frase no modelo spacy
    doc = nlp(frase)

    #sem as palavras irrelevantes
    frase2 = principal.RemoverIrrelevantes(frase)
    doc2 = nlp(frase2)


    # Gerar dataset das dependecias
    dep_palavra = []
    for token in doc:
        while token.head != token:
            x = token.text
            dep_palavra.append(x)
            token = token.head

    # Gerar dataset das dependecias sem as palavras irrelevante
    dep_PalvraIrr = []
    if len(frase2.split()) > 1 :
        for token in doc2:
            while token.head != token:
                x = token.text
                dep_PalvraIrr.append(x)
                token = token.head
    else:
        dep_PalvraIrr.append(frase2)




    maiorfreq = FreqDist(item for item in dep_palavra)
    maiorfreq2 = FreqDist(item for item in dep_PalvraIrr)

    mf1 = maiorfreq.most_common(1)
    mf2 = maiorfreq2.most_common(1)

    if mf1 == mf2:
        return mf1
    else:
        return ValidarNucleos(frase, mf1[0][0], mf2[0][0])



def ValidarNucleos(frase, p1, p2):
    ind1 = frase.index(p1)
    ind2 = frase.lower().index(p2)

    if ind1 < ind2:
        end = ind2+len(p2)
        start = ind1
    else:
        end = ind1 +len(p1)
        start = ind2
    return frase[start:end]



def TipoNucleo(nucleo):
    resposta = "R"
    palavraChave = ["solicitar", "necessitar", "precisar", "carecer","exigir","exijir",
        "requerer",        "demandar",
        "pedir",        "reclamar",
        "dever",        "ter que",
        "Querer" ,       "ter de"
    ]

    radicalTarget = [ principal.Radical(i) for i in palavraChave]
    try:
        radicalNucleo = principal.Radical(nucleo.lower())
    except:
        radicalNucleo = principal.Radical(nucleo[0][0].lower())

    for item in radicalTarget:
        if item in radicalNucleo:
            resposta = "B"

    return resposta
