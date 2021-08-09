#para instalar a biblioteca: pip install pywhatkit
import pywhatkit as kt

iDIRETORIO = "C:/Users/pinheiro/Documents/Youtube/AsciiImage/" #diretorio que contem as imagens
iIMAGEMS = ["sonic.jpg","github.jpg","mario.png"] #lista de imagens a serem convertidas

#a cada imagem ira gerar um arquivo TXT com o conteudo convertido em ASCII
for iIMG in iIMAGEMS:
    kt.image_to_ascii_art(iDIRETORIO + iIMG, iDIRETORIO + iIMG.split(".")[0] )

