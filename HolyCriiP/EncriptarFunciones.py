import os
from cryptography.hazmat.primitives.hashes import *
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.ciphers import algorithms, modes,  Cipher
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import hashlib, sys, math, getpass
from Files import *
from Functions import *

def blocksKey():
    #Genera y devuelve la clave que define el tamanio de bloques
    print("Insert Principal Key")
    keyUserInput = getpass.getpass().encode('ascii')
    padder = padding.PKCS7(128).padder() #Implement for AES crypt
    padded_data = padder.update(keyUserInput)
    padded_data += padder.finalize()
    hash = hashlib.sha256()
    hash.update(keyUserInput)
    finalKey = hash.hexdigest()
    finalKeyNumber = converHashToNum(finalKey)
    #Falta integrar validar largo de password
    return [padded_data, finalKeyNumber]

def rangeKey():
    #Genera y devuelve la clave que define el rango de bloques a tomar
    print("Insert a Second key (must be 4 digits, only numbers)")
    keyUserInput = getpass.getpass('Key:')
    keyAcumulator = 0
    for i in range(4):
        keyAcumulator = keyAcumulator + int(keyUserInput[i])
    padder = padding.PKCS7(128).padder() #Mask for represent 128bits block with unique second key
    keyUserInput = bytes(keyUserInput.encode('ascii'))
    keyMask16 = padder.update(keyUserInput) #Implement for AES Crypt
    keyMask16 += padder.finalize()
    #For xor crypt
    if ( int(keyUserInput[1]) != 0):
        secondKey = keyAcumulator * int(keyUserInput[1])
    while (secondKey > 123):
        secondKey = secondKey / 2
        secondKey = int(math.floor(secondKey))
            #falta interactuar la clave con la primaria para ampliar el espectro
    return [keyAcumulator, keyMask16, secondKey]

def cryptorAES(key1, key2, word):
    #Genera la encriptacion o la deshace si se encuentra encriptado y las claves son identicas
    #word: debe ser el dato en BYTES a cifrar
    '''This not working yet. Don't use it'''
    backend = backends.default_backend()
    cipher = Cipher(algorithms.AES(key1), modes.CBC(key2), backend)
    encryptor = cipher.encryptor()
    wordCrypter = encryptor.update(word) + encryptor.finalize()
    return wordCrypter

def holyCryptor(file, sizeBlock, rang, secondKey, mode):
    #It take the size of file and calculate how many block exist for this key/file
    file.seek(0,2)
    fileSize = file.tell()
    qBlocks = fileSize / sizeBlock #Quantity block for file and key
    qBlocks = math.floor(qBlocks)
    turns = qBlocks / rang
    turns = math.floor(turns)
    restBytes = fileSize - (turns * rang * sizeBlock) #Se multiplica asi por los redondeos
    fileCrypt = tempfile.TemporaryFile()
    counter = 0
    i = 1
    while (i < (turns + 1)):
        control = rang -1
        startControl = (i -1) * sizeBlock * rang
        while ((control+1) > 0):
            file.seek((sizeBlock*control) + startControl, 0)
            data = file.read(sizeBlock)
            fileCrypt.seek(counter * sizeBlock, 0)
            fileCrypt.write(data)
            counter =  counter + 1
            control = control - 1
        i = i + 1
    #Opera con los restantes
    file.seek((-1 * restBytes), 2)
    data = file.read(restBytes)
    fileCrypt.seek(0,2)
    fileCrypt.write(data)
    file.close()

    return fileCrypt

