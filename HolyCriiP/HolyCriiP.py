from EncriptarFunciones import *
from Files import *
from Functions import *

fileRoute = fileSearch()
fileOpen = abrirArchivo(fileRoute)
primaryKey = blocksKey()
range = rangeKey()
fileCrypt = holyCryptor (fileOpen, primaryKey[1], range[0], range[2], 0)
#fileOverwrite(fileRoute, fileCrypt) # Mode without XOR pass, not recommend for text files
#fileOverwriteWithXOR(fileRoute, fileCrypt, range[2]) # Mode with XOR, is slowly but effective against text file
fileOverwriteThreadingWithXOR(fileRoute, fileCrypt, range[2]) # In this mode the encryption is 13% more quick (approx)

print ("Encriptacion finalizada")