import tempfile
import os

def fileSearch():
    #Devuelve la ruta y el nombre del archivo a encriptar
    #This function return the route and name of the file to encrypt
    fileName = input("Ingrese el nombre del archivo: ")
    fileName = os.path.abspath(fileName)
    fileName = fileName.replace("\\", "/") 
    #Falta validar si existe O NO. FALTANTE.
    return fileName

def abrirArchivo(ruta):
    print(ruta)
    archivo = open(ruta, "r+b")
    return archivo

def fileOverwrite (filePath, fileCrypt):
    fileCrypt.seek(0,0)
    fileToOverwrite = open(filePath, "wb")
    data = fileCrypt.read()
    fileToOverwrite.write(data)
    fileCrypt.close()
    fileToOverwrite.close()
    renameFile(filePath)

def fileOverwriteWithXOR (filePath, fileCrypt, xorKey):
    fileSize = os.path.getsize(filePath)
    fileCrypt.seek(0,0)
    #   secondKey = secondKey.to_bytes(secondKey.bit_length(), byteorder = sys.byteorder) Don't uncomment this
    #   But, don't delete too, is my project anyway.
    data = bytearray(fileCrypt.read())
    fileToOverwrite = open(filePath, "wb")
    for i in range(len(data)):
        data[i] ^= xorKey
    fileToOverwrite.write(data)
    #Files closed
    fileCrypt.close()
    fileToOverwrite.close()
    renameFile(filePath)

def renameFile (filePath):
    if ('.hc' in filePath):
        newName = filePath.rstrip('.hc')
        os.rename(filePath, newName)
    else:
        newName = filePath + '.hc'
        os.rename(filePath, newName)