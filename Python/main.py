import Arquivo as arq
import principal
import nucleoSpacy as ns
import funcaoGramatical


frase ='O pensamento tem muito poder, muitas vezes aquilo que pensamos pode se realizar.'
media = 0
ml = principal.Invoke(frase)
tpn = ns.TipoNucleo(ns.RetornNucleo(frase))
fg = funcaoGramatical.Morfologia(frase)


if ml == 'B':
    media = 1

if tpn == 'B':
    media = media + 1


if fg == 'B':
    media = media + 1



fileName = '../Data/leandro.csv'
array = [media,ml,tpn,fg]
cabecalho = 'Media,MAchineLearing,Classificação Nucleo, Função gramatical'


# Gerar Arquico
arq.GerarArquivoCSV(fileName,array,cabecalho)
