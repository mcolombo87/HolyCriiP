import threading, Monitor, Files

class XorThread(threading.Thread):

    def __init__(self, num, fileToOverwrite, dataRead, xorKey, event, monitor):
        threading.Thread.__init__(self)
        self.num = num
        self.fileToOverwrite = fileToOverwrite
        self.dataRead = dataRead
        self.xorKey = xorKey
        self.event = event
        self.monitor = monitor

    def run(self):

        print ("Starting {}".format(self.num))
        xorProcess(self)
        print ("Exiting {}".format(self.num))

def xorProcess(self):

        data = bytearray(self.dataRead)
        print ("Thread in XOR {}".format(self.num))
        for i in range(len(data)):
            data[i] ^= self.xorKey
        writeFileThread(self, data)

def writeFileThread(self, data):

    print ("Thread Wait {}".format(self.num))
    self.monitor.requestAccess(self.num)
    print ("Thread Write {}".format(self.num))
    self.fileToOverwrite.write(data)
    self.monitor.reportFinally(self.num)
