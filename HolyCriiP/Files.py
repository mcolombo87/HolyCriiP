import tempfile, math, threading
import os, XorThread, Monitor

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
    data = bytearray(fileCrypt.read())
    fileToOverwrite = open(filePath, "wb")
    for i in range(len(data)):
        data[i] ^= xorKey
    fileToOverwrite.write(data)
    #Files closed
    fileCrypt.close()
    fileToOverwrite.close()
    renameFile(filePath)

def fileOverwriteThreadingWithXOR (filePath, fileCrypt, xorKey):

    fileSize = os.path.getsize(filePath)
    fileToOverwrite = open(filePath, "wb")
    fileCrypt.seek(0,0)
    lengthToCatch = fileSize / 4
    lengthToCatch = int(math.floor(lengthToCatch))
    counter = 0
    thNumb = 1 #assigned number to each new thread
    threads = [] #list of threads
    xMonitor = Monitor.Monitor(1,threads)
    xMonitor.start()
    while (counter < fileSize):
        #llamo al thread (paso lengthToCatch)
        dataRead = bytearray(fileCrypt.read(lengthToCatch)) #Read data for temporary File encrypted
        event = threading.Event()
        xThread = XorThread.XorThread(thNumb, fileToOverwrite, dataRead, xorKey, event, xMonitor) #New thread
        xMonitor.setNewThreadInList(xThread) #Storing thread on list
        #threads.append(xThread)
        xThread.start()
        if ((counter+(lengthToCatch*2)) > fileSize ):
            counter += lengthToCatch
            lengthToCatch = fileSize - counter
        else:
            counter += lengthToCatch
        fileCrypt.seek(counter, 0)
        thNumb += 1
    #Files closed
    for t in xMonitor.getThreadList():
        t.join()    #Waiting until the threads terminates
    print ("Exiting Main Thread") 
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

