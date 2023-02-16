#Integrantes:
# Heitor
# Lucas Lima
# Rafael Camara
# Vithor Veronese
import sys

def saveBackup(fileContents, fileName):
    newName = fileName.replace(".txt", "") + "_backup.txt"
    backup = open(newName, "w")
    backup.write(fileContents)
    backup.close()

def circularAlfabet(number):
    if (number > 128):
        return number - 128
    elif (number < 0):
        return number + 128
    else:
        return number

def caesarCipher(oldContent, key):
    newContent = ""
    for char in oldContent:
        asciiNumber = ord(char.encode(encoding="ascii")) + key
        newChar = chr(circularAlfabet(asciiNumber))
        newContent += newChar
    return newContent

def presentMessage(key):
    if (key < 0):
        print("\n\nAgradecemos sua participação! Nos veremos novamente\n\n")
    else:
        print("\n\n SEU ARQUIVO FOI ENCRIPTADO\n\n MANDE 10.000 (DEZ MIL) BITCOINS PARA A CARTEIRA X \n\n")

def handleFile(fileName, key):
    #Linhas 25-26 (try e with) e 42-44 (except IOError) foram pegas do chatGPT
    try:
        with open(fileName, "r", encoding="utf-8") as f:
            content = f.read()
            f.close()
            newContent = caesarCipher(content, key)
            if (key > 0): 
                saveBackup(content, fileName)
            newFile = open(fileName, "w")
            newFile.write(newContent)
            newFile.close()
            presentMessage(key)
    
    except IOError:
        print("Erro: arquivo não encontrado ou não pode ser lido\n")
        sys.exit()
    # except UnicodeEncodeError:
    #     print("Erro na codificação do documento")
    #     sys.exit()

def main():
    filename = input("\nDigite o nome do arquivo a ser (de)criptado, ou o seu endereço completo: ")
    key = int(input("Digite a chave de encriptação (valor positivo significa encriptar, valor negativo decriptar): "))
    handleFile(filename, key)

main()
