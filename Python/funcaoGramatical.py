import nltk

def Morfologia(frase):
    verbo = 0
    substantivos = 0
    frasex = frase.split()

    funcao  = []

    token  = nltk.pos_tag(frasex)
    partPort = {"YES_NO_SENT": 1, "Z": 1,  # Desconhecidos
                "PTCL": 2, "PRT": 2,  # "Outras palavras de funcao"
                "EX": 3, "FW": 3, "MD": 3,  # "existencial","palavra estrangeira","auxiliar modal"
                "NC": 4, "CD": 4,  # Numerais
                "JJ": 10, "JJR": 10, "JJS": 10, "A": 10,  # Adjetivos
                "NNP": 6, "NNPS": 6, "NNS": 6, "NN": 6,  # Substantivos
                "DET": 7, "DT": 7, "PDT": 7, "WDT": 7,  # Determinantes
                "POS": 8, "LS": 8,  # Marcadores
                "PRP": 9, "PRP$": 9, "WP$": 9, "WP": 9, "P": 9,  # Pronomes
                "WRB": 10, "RB": 10, "RBR": 10, "RBS": 10, "AD": 10,  # Adjetivos
                "RP": 11, "SYM": 11, "UH": 11,  # "particula", "simbolo", "interjeicao"
                "COMP": 12, "C": 12, "CC": 12,  # "Conjuncoes"
                "TO": 13, "IN": 13, "ADP": 13,  # Preposições
                "V": 14, "VG": 14, "VI": 14, "VP": 14, "VB": 14, "VBD": 14, "VBG": 14, "VBN": 14, "VBP": 14, "VBZ": 14 # Verbos
                # Verbo
                }

    for item in token:
        funcao.append(partPort.get(item[1]))

    for x in funcao:
        if x == 14:
            verbo = 1
        if x == 6:
            substantivos = 1

    if verbo > 0 and substantivos > 0:
        return 'B'
    else:
        return 'R'




