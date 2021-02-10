import csv
import os

def GerarArquivoCSV(fileName,array,cabecalho):
    # prepara cabeçalho
    arrSplit = cabecalho.split(",")
    arrCabec = [i for i in arrSplit]

    # Remove  arquivo
    DeletarArquivo(fileName)

    with open(fileName, 'w', newline='') as file:
        #Criar o separador de colunas
        csv.register_dialect("pv", delimiter=';')

        # intancia o arquivo
        arquivo =  csv.writer(file, dialect="pv")
        # Escrever no arquivo
        arquivo.writerow(arrCabec)
        arquivo.writerow(array)

    # Fechar o arquivo
    file.close()



def  DeletarArquivo(fileName):
    # Verificar se o arquivo existe
    if os.path.exists(fileName):
        # Deletar o arquivo
        os.remove(fileName)


def AdicionarLinha(array, fileName):
    # Abrir Arquivo
    with open(fileName, 'a') as file:
        #Criar o separador de colunas
        csv.register_dialect("pv", delimiter=';')

        # intancia o arquivo
        arquivo =  csv.writer(file, dialect="pv", lineterminator='\n')
        # Escrever no arquivo
        arquivo.writerow(array)

    # Fechar o arquivo
    file.close()