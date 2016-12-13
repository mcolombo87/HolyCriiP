from EncriptarFunciones import *
from Files import *
from Functions import *


fileRoute = fileSearch()
fileOpen = abrirArchivo(fileRoute)
primaryKey = blocksKey()
range = rangeKey()
fileCrypt = holyCryptor (fileOpen, primaryKey[1], range[0], range[2], 0)
print("-Methods-")
print("1. Mode without XOR pass, not recommended for text files")
print("2. Mode with XOR, is slowly but effective against text file")
print("3. In this mode the encryption is 13% more quick (approx)")
selection = input("Choose one method: ")
if (int(selection) == 1):
    fileOverwrite(fileRoute, fileCrypt) # Mode without XOR pass, not recommend for text files
if (int(selection) == 2):
    fileOverwriteWithXOR(fileRoute, fileCrypt, range[2]) # Mode with XOR, is slowly but effective against text file
if (int(selection) == 3):
    fileOverwriteThreadingWithXOR(fileRoute, fileCrypt, range[2]) # In this mode the encryption is 13% more quick (approx)

print ("Encriptacion finalizada")
os.system("PAUSE")