from EncriptarFunciones import *
from Files import *
from Functions import *

fileRoute = fileSearch()
fileOpen = abrirArchivo(fileRoute)
primaryKey = blocksKey()
range = rangeKey()
#print("PruebaMask: %d", range[1])
#prueba = fileOpen.read(128)
#print (prueba)
#print(sys.getsizeof(primaryKey))
#print(sys.getsizeof(range[1]))
#testrandom = os.urandom(32)
#print(testrandom)
#print(sys.getsizeof(testrandom))
#test2 = cryptor(primaryKey,range[1], prueba)
#print (test2)
fileCrypt = holyCryptor (fileOpen, primaryKey[1], range[0], range[2], 0)
#fileOverwrite(fileRoute, fileCrypt)
fileOverwriteWithXOR(fileRoute, fileCrypt, range[2])

print ("Encriptacion finalizada")